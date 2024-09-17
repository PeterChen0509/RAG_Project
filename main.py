from cleaning import find_jp_md_files, process_md_files, chunk_md_files
from embedding import create_vectorstore, rrf_retriever, load_vectorstore, create_prompt, generate_answer, create_chat_model, query_generator
from eval import filtered_keywords, extract_technical_terms, generate_final_answer
from search import get_best_answer
from collections import defaultdict
import pandas as pd

root_dir = "/home/Preda/user/Sony_InternProj/content"
vector_db_path = "/home/Preda/user/Sony_InternProj/data/vectordb"
file_path = "/home/Preda/user/Sony_InternProj/data/マニュアルQA正解データ.xlsx"
model = create_chat_model()

keywords = filtered_keywords()
keywords_lower = [kw.lower() for kw in keywords]

jp_md_files = find_jp_md_files(root_dir)
all_chunks = process_md_files(jp_md_files)
all_chunks = chunk_md_files(all_chunks)
# print("all_chunks[15]: ", all_chunks[15])
print("len(jp_md_files):", len(all_chunks))
if vector_db_path:
    vector_db = load_vectorstore(vector_db_path)
else:
    vector_db = create_vectorstore(chunks=all_chunks)


def process_queries(file_path, model, keywords_lower):
    df = pd.read_excel(file_path)
    df["仮想質問"] = df["質問"].apply(lambda x: query_generator(x, model)) # Relevant 4 queries
    df["関連情報"] = df["質問"].apply(lambda x: rrf_retriever(x, vector_db, model, top_k=5, top_f=10)) # Top-10 results
    df["単純にRAGの答えを参考にする"] = df["質問"].apply(lambda x: generate_answer(create_prompt(rrf_retriever(x, vector_db, model, top_k=5, top_f=10), x), model))
    df["専門用語"] = df["単純にRAGの答えを参考にする"].apply(lambda x: extract_technical_terms(x)) # Extract technical terms from the primary answer
    df["マニュアルに説明されていない専門用語"] = df["専門用語"].apply(lambda x: [tech for tech in x if not any(keyword in tech.lower() for keyword in keywords_lower)]) # Filter out terms not explained in manual

    def handle_unmatched(row):
        # Generate the final answer considering the unexplained term by manual
        unmatched = row["マニュアルに説明されていない専門用語"]
        data = defaultdict(lambda: {"url": "", "match": ""})
        for unmatch in unmatched:
            best_match, best_url = get_best_answer(unmatch)
            data[unmatch]["url"] = best_url
            data[unmatch]["text"] = best_match
        return generate_final_answer(row["単純にRAGの答えを参考にする"], data, model)

    df["最終回答"] = df.apply(handle_unmatched, axis=1)
    return df


df = process_queries(file_path, model, keywords_lower)
df.to_excel("/home/Preda/user/Sony_InternProj/data/マニュアルQA(最終RAG).xlsx", index=False)
print(df.head())










# query = "Neural Network Consoleではできないが、PredictionOneだとできる、または容易にできることはありますか？"
# # each query will return top 5 results, one query will generate 4 relevant query
# # finally use top-10 results to generate the final answer
# rrf_ranked_results = rrf_retriever(query, vector_db, model, top_k=5, top_f=10)

# prompt = create_prompt(rrf_ranked_results, query)
# answer = generate_answer(prompt, model)
# print("答案:", answer)

# tech_keywords = extract_technical_terms(answer)
# unmatched = [tech for tech in tech_keywords if not any(keyword in tech.lower() for keyword in keywords_lower)]
# print("unmatched:", unmatched)

# data = defaultdict(lambda: {"url": "", "match": ""})
# for unmatch in unmatched:
#     best_match, best_url = get_best_answer(unmatch)
#     data[unmatch]['url'] = best_url
#     data[unmatch]['text'] = best_match
 
# print(len(data))

# final_answer = generate_final_answer(answer, data, model)
# print("最終の回答:", final_answer)

# df = pd.read_excel(file_path)