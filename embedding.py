from typing import Optional, Any, List
import time, datetime
from dotenv import load_dotenv
import os
import re
import numpy as np
import faiss
from langchain_openai import AzureChatOpenAI, AzureOpenAIEmbeddings
from langchain_community.vectorstores.faiss import FAISS

load_dotenv()

def create_embeddings_model(
    model_name = "text-embedding-3-large",
    chunk_size: int = 2048,
    api_key = os.environ["OPENAI_API_KEY"],
    api_version = "2024-02-01",
    azure_endpoint = "https://azure-preone-openai-sweden-central-01-chen.openai.azure.com/",
):
    # Create an AzureOpenAIEmbeddings model
    return AzureOpenAIEmbeddings(
        model=model_name,
        chunk_size=chunk_size,
        api_key=api_key,
        api_version=api_version,
        azure_endpoint=azure_endpoint,
    )

def create_chat_model(
    model_name = "gpt-4o",
    api_key = os.environ["OPENAI_API_KEY"],
    api_version = "2024-02-01",
    temperature: float = 0,
    azure_endpoint = "https://azure-preone-openai-sweden-central-01-chen.openai.azure.com/",
):
    # Create an AzureChatOpenAI model
    return AzureChatOpenAI(
        model=model_name,
        api_key=api_key,
        api_version=api_version,
        azure_endpoint=azure_endpoint,
        temperature=temperature,
    )

def create_vectorstore(
    chunks: List[Any],
    batch_size: int = 100,
    retry_delay: int = 60,
):
    # Create a vector store from chunks

    print("Start creating vector store")
    start_time = time.time()
    embedding = create_embeddings_model(chunk_size=2048)
    vectordb = None
    for i in range(0, len(chunks), batch_size):
        batchs = chunks[i: i+batch_size]
        documents = [
            {
                "page_content": (
                    f"Title: {batch.metadata.get('title', '')} \n"
                    f"Description: {batch.metadata.get('description', '')} \n"
                    f"Keywords: {', '.join(batch.metadata.get('keywords', []))} \n"
                    f"Subtitle: {batch.metadata.get('subtitle', '')} \n"
                    f"Content: {batch.page_content}"
                ),
                "metadata": batch.metadata
            }
            for batch in batchs
        ]
        while True:
            try:
                total_batches = (len(chunks)+batch_size-1)//batch_size
                current_batch = i//batch_size+1
                print(f"Processing batch {current_batch}/{total_batches}")
                if vectordb is None:
                    vectordb = FAISS.from_texts(
                        [doc["page_content"] for doc in documents],
                        embedding=embedding,
                        metadatas=[doc["metadata"] for doc in documents],
                    )
                else:
                    vectordb.add_texts(
                        [doc["page_content"] for doc in documents],
                        metadatas=[doc["metadata"] for doc in documents],
                    )
                break
            except Exception as e:
                print(f"Error processing batch: {e}")
                print(f"Retrying in {retry_delay} seconds")
                time.sleep(retry_delay)
                retry_delay *= 2
    if vectordb:
        export_db_path = f"/home/Preda/user/Sony_InternProj/data/vectordb"
        vectordb.save_local(export_db_path)
    
    end_time = time.time()
    print(f"Vector store created in {end_time-start_time} seconds")

    return vectordb

def load_vectorstore(path):
    # Load a local vector store
    embeddings = create_embeddings_model()
    vectordb = FAISS.load_local(path, embeddings, allow_dangerous_deserialization=True)
    return vectordb

def query_generator(query, model):
    # Generate multiple search queries related to the original query

    print(f"Start generating queries for: {query}")
    start_time = time.time()

    prompt = (
        "あなたは役に立つアシスタントです。日本語で検索クエリを生成してください。\n"
        "次の内容に関連する4つの異なる検索クエリを生成してください：{query}。\n"
        "各クエリは新しい行に表示されます。\n"
        "クエリを生成する際、元の意味を大きく変えずに、関連する追加のコンテキストを日本語で追加してください。"
    ).format(query=query)
    response = model.generate([prompt], timeout=30)
    queries = response.generations[0][0].text.strip().split("\n")
    queries = [re.sub(r"^\d+\.\s*", "", q.strip()) for q in queries if q.strip()]

    end_time = time.time()
    print(f"Queries generated in {end_time - start_time:.2f} seconds")

    return queries

def normalize_vectors(vectors):
    # Normalize vectors to calculate cosine similarity
    vectors = vectors.reshape(1,-1)
    faiss.normalize_L2(vectors)
    vectors = vectors.reshape(-1)
    return vectors

def reciprocal_rank_fusion(results: List[List[Any]], k: int = 60) -> List[Any]:
    # Calculate reciprocal rank fusion for multiple queries
    fusion_scores = {}
    for docs in results:
        for rank, doc in enumerate(docs):
            doc_str = f"{doc.metadata.get('source_path', '')}_{doc.metadata.get('chunk_id', '')}"
            if doc_str not in fusion_scores:
                fusion_scores[doc_str] = 0
            fusion_scores[doc_str] += 1 / (rank+k)
    reranked_results = sorted(fusion_scores.items(), key=lambda x: x[1], reverse=True)
    reranked_docs = []
    for doc_str, score in reranked_results:
        for docs in results:
            for doc in docs:
                if f"{doc.metadata.get('source_path', '')}_{doc.metadata.get('chunk_id', '')}" == doc_str:
                    reranked_docs.append(doc)
                    break
    return reranked_docs

def rrf_retriever(query, vectordb, model, top_k: int = 5, top_f: int = 10):
    # Retrieve documents using FAISS for each similar query and rerank using RRF
    print(f"Start retrieving documents for query: {query}")
    start_time = time.time()

    queries = query_generator(query, model)
    results = []
    for idx, q in enumerate(queries):
        print(f"Processing query {idx+1}/{len(queries)}: {q}")
        query_vector = create_embeddings_model().embed_query(q)
        query_vector = np.array(query_vector).astype('float32')
        query_vector = normalize_vectors(query_vector)

        search_start_time = time.time()
        result = vectordb.similarity_search_by_vector(query_vector, k=top_k)
        search_end_time = time.time()

        print(f"Search completed in {search_end_time - search_start_time:.2f} seconds")
        results.append(result)
    reranked_results = reciprocal_rank_fusion(results, k=top_k)
    end_time = time.time()
    print(f"Document retrieval completed in {end_time - start_time:.2f} seconds")
    return reranked_results[:top_f]

# def query(query, vectordb):
#     # Query the vector datastore using RAG Fusion
#     reranked_doc = rrf_retriever(query, vectordb)

def create_prompt(documents: List, query: str) -> str:
    # Create a prompt for the user to answer a question
    if not documents:
        return f"質問に対して適切な参考情報が見つかりませんでした。質問：{query}\n"
    prompt = f"質問に対して、以下の情報を踏まえ、具体的かつ詳細に回答してください：{query}\n\n"
    prompt += "参考情報：\n"
    for doc in documents:
        prompt += f"- {doc.page_content}\n" 
    prompt += "\n回答を作成する際の指示：\n"
    prompt += "1. 質問を繰り返さず、直接的な答えを提供してください。\n"
    prompt += "2. 関連する詳細や理由を含め、簡潔かつ論理的に回答してください。\n"
    prompt += "3. 回答は明確で、質問の重要なポイントを網羅してください。\n"
    prompt += "4. 情報不足を避けるため、答えを適度な長さに保ってください。\n"
    prompt += "5. 回答には無駄な表現やまとめの言葉を避け、質問に対する最適な情報を提供してください。\n"
    return prompt

def generate_answer(prompt, model):
    # Generate answer using the prompt
    response = model(
        messages=[
            {"role": "system", "content": "あなたは簡潔で直接的な回答を提供する専門家です。不要な説明や前置きを避け、質問に対して即座に核心を突いた回答をします。"},
            {"role": "user", "content": prompt}
        ]
    )
    return response.content
