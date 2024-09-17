from googlesearch import search
from bs4 import BeautifulSoup
import requests
import nltk
import numpy as np
import unicodedata
from retrying import retry
from fake_useragent import UserAgent
import os
import time
from langchain_openai import AzureOpenAIEmbeddings
from typing import List, Tuple, Optional

nltk.download('punkt')

class GoogleSearcher:
    def __init__(self, query: str, max_results: int = 5) -> None:
        self.query = query
        self.max_results = max_results
        self.user_agent = UserAgent()

    @retry(stop_max_attempt_number=3, wait_fixed=2000)
    def fetch_links(self) -> List[str]:
        # Get search result links
        try:
            return list(search(self.query, lang="ja", stop=self.max_results))
        except Exception as e:
            print(f"Error fetching links: {e}")
            return []
    
    def fetch_content(self, url: str) -> str:
        # Fetch content from a URL
        try:
            headers = {"User-Agent": self.user_agent.random}
            response = requests.get(url, headers=headers, timeout=5)
            response.raise_for_status()
            soup = BeautifulSoup(response.content, "html.parser")
            return soup.get_text(strip=True)
        except Exception as e:
            print(f"Error fetching {url}: {e}")
            return ""
    
class SemanticSearcher:
    def __init__(self, api_key: str, endpoint: str, api_version: str):
        self.embedding_model = AzureOpenAIEmbeddings(
            model="text-embedding-3-large",
            api_key=api_key,
            azure_endpoint=endpoint,
            api_version=api_version
        )


    def get_embedding(self, text: str) -> np.ndarray:
        # Encode query into vector
        try:
            return np.array(self.embedding_model.embed_query(text))
        except Exception as e:
            print(f"Error in embedding generation: {e}")
            return np.random.rand(1536)
        
    def find_best_match(self, query: str, documents: List[str]) -> Tuple[str, float]:
        # Only return the most similar document and its similarity score
        query_embedding = self.get_embedding(query)
        best_match = max(documents, key=lambda doc: np.dot(query_embedding, self.get_embedding(doc)) / (np.linalg.norm(query_embedding) * np.linalg.norm(self.get_embedding(doc))))
        similarity = np.dot(query_embedding, self.get_embedding(best_match)) / (np.linalg.norm(query_embedding) * np.linalg.norm(self.get_embedding(best_match)))
        return best_match, similarity

def get_best_answer(query: str, min_char_len: int = 100) -> Optional[Tuple[str, str]]:
    # Get only the result with the most relevant to query
    start_time = time.time()

    search_query = f"{query} とは"  # Add explanatory keywords to the query
    google_searcher = GoogleSearcher(search_query)
    links = google_searcher.fetch_links()

    if not links:
        print("No search results found.")
        return None
    
    documents, urls = [], []
    for url in links:
        content = google_searcher.fetch_content(url)
        if len(content) >= min_char_len and any(keyword in content for keyword in ["とは", "解説", "説明"]):
            documents.append(content)
            urls.append(url)
        if len(documents) >= 5:
            break

    if not documents:
        print("No document content found.")
        return None

    semantic_searcher = SemanticSearcher(
        api_key=os.environ['OPENAI_API_KEY'],
        endpoint="https://azure-preone-openai-sweden-central-01-chen.openai.azure.com/",
        api_version="2024-02-01"
    )

    best_match, similarity = semantic_searcher.find_best_match(query, documents)
    best_url = urls[documents.index(best_match)]

    end_time = time.time()
    elapsed_time = end_time - start_time

    print(f"Best match (URL: {best_url}): {best_match[:500]}...")
    print(f"Time taken for retrieving the best answer: {elapsed_time:.2f} seconds")
    return best_match, best_url
