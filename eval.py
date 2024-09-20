from embedding import (
    create_chat_model,
    create_embeddings_model
)
from datasets import Dataset
from ragas import evaluate
from langchain.docstore.document import Document
from typing import List
from ragas.metrics import (
    context_precision,
    answer_relevancy,
    faithfulness,
    answer_correctness,
)
from transformers import BertJapaneseTokenizer
from nltk.translate.meteor_score import meteor_score
import pandas as pd
from sudachipy import dictionary, tokenizer
import re
import time

def filtered_keywords():
    keywords = [
    'AI', 'API', 'API KEY', 'AUC', 'Accuracy', 'Additional Info API', 'DB', 
    'LLM', 'OS', 'Precision', 'REST API', 'ROC', 'ROCAUC', 'Train', 
    'Train Status Check', 'apikey', 'bash', 'classify', 'credential', 'csv', 
    'cui', 'feature selection', 'fvalue', 'importance', 'join', 'log in', 
    'login', 'missing value', 'preprocess', 'PredictionOne', 'retrain model switch', 
    'retrain status check', 'root mean squared error', 'secret key', 'test', 
    'train', 'train status check', 'tsv', 'update', 'valid', 'xlsx', 
    'アンサンブル', 'クロスバリデーション', 'グラフ', 'シークレットキー', 'チューニング', 'データ', 
    'データサイエンス', 'データセット', 'データ分析', 'データ加工', 'データ結合', 'トレーニングデータセット', 
    'ドリフト', 'ハイパーパラメータ探索', 'バギング', 'バイナリ', 'パラメタ', 'プロット', '機械学習', 
    '教師あり学習', '欠損', '混同行列', '精度', '精度向上', '精度改善', '精度評価', '特徴', 
    '特徴選択', '自然言語処理', '過学習', '交差検証', '関連度スコア', '閾値', 'モデルの更新', 
    '予測API', '予測モデル', '予測モデル作成', '予測寄与度', '予測精度', '学習', '学習API', 
    '学習データ', '学習失敗', '学習実行時間', '教師データ', 'リグレッション'
    ]
    return keywords


def get_ragas_score(
        question_list, answer_list, context_list, ground_truth_list
):
    # Get ragas score
    ds = Dataset.from_dict(
        {
            "question": question_list,
            "answer": answer_list,
            "contexts": context_list,
            "ground_truths": ground_truth_list,
        }
    )
    metrics = [
        faithfulness,
        answer_relevancy,
        context_precision,
        answer_correctness,
    ]
    result = evaluate(
        ds,
        metrics=metrics,
        llm=create_chat_model(),
        embeddings=create_embeddings_model(),
    )
    return result

def meteor_score(ground_truth, generated):
    # Calculate METEOR score
    tokenizer = BertJapaneseTokenizer.from_pretrained("cl-tohoku/bert-base-japanese-whole-word-masking")
    tokenized_ground_truth = [[tokenizer.tokenize(ref) for ref in refs] for refs in ground_truth]
    tokenized_answer = [tokenizer.tokenize(ans) for ans in generated]
    meteor_scores = [meteor_score(refs, ans) for refs, ans in zip(tokenized_ground_truth, tokenized_answer)]
    return meteor_scores

def extract_technical_terms(text):
    # Using GPT to extract technical terms
    print(f"Start extracting technical terms from the provided text.")
    start_time = time.time()
    model = create_chat_model()
    
    prompt = f"""
    以下の文には、コンピュータサイエンス、機械学習、統計学、データ分析に関する高度な専門用語や専有名詞が含まれています。
    次の基準に従って、専門用語および関連するツール、ソフトウェア、サービスの名称をリストアップしてください：

    1. 統計的手法や評価指標（例：RMSE、F値、交差検証）
    2. 機械学習のアルゴリズムや特定の手法（例：サポートベクターマシン、ランダムフォレスト）
    3. 数学的概念や計算方法（例：二乗平均平方根、平方根）
    4. 特殊な分析手法や概念（例：主成分分析、過学習）
    5. ソフトウェア、ツール、プラットフォーム、サービスの名称（例：Neural Network Console、TensorFlow、PredictionOne）
    
    以下の種類の用語は除外してください：
    - 一般的なデータ分析用語（例：サンプル、データ、モデル）
    - 業務や対象を表す一般的な用語（例：顧客データ、予測モデル）
    - 一般的なプロセスを表す用語（例：学習用データ、評価用データ）

    専門用語と特定のソフトウェア名やサービス名のみを、リスト形式で、番号や説明文なしで列挙してください。各専門用語は1行に1つのみ表示してください。
    文脈上重要でない単語や、上記の除外すべき用語は絶対に含めないでください。

    テキスト：
    {text}
    """
    try:
        response = model(
            messages=[
                {"role": "user", "content": prompt}
            ],
            timeout=30
        )
        terms_text = response.content
        terms = terms_text.strip().split("\n")
        terms = [term.strip() for term in terms if term.strip()]
        end_time = time.time()
        print(f"Technical terms extracted in {end_time - start_time:.2f} seconds")
    except Exception as e:
        print(f"Error extracting technical terms: {e}")
        return []
    return terms


def remove_special_terms(text, terms):
    # Remove special terms from text to calculate Term Density
    for term in terms:
        text = text.replace(term, '')
    tokenizer_obj = dictionary.Dictionary().create()
    tokens = [m.surface() for m in tokenizer_obj.tokenize(text, tokenizer_obj.SplitMode.B)]
    tokens = [token for token in tokens if token.strip()]
    return tokens

def calculate_term_density(text):
    # Calculate term density
    terms = extract_technical_terms(text)
    tokens = remove_special_terms(text, terms)
    term_density = len(terms) / (len(terms)+len(tokens)) * 100
    print(f"専門用語の割合: {term_density:.2f}%")
    return term_density

def create_combined_prompt(answer, data):
    # Create a combined prompt for the terms and answer
    combined_prompt = f"以下は質問に対する初期の回答です: \n{answer}\n\n"
    combined_prompt += f"以下の専門用語の詳細な説明と出典が含まれています。これらの説明を用いて、最終的な回答を生成してください。回答には必要な説明を統合し、出典も含めてください。専門用語を個別にリストしないで、全体的に流れるように回答に組み込んでください。\n"
    for term, info in data.items():
        combined_prompt += f"\n{info['text']}（出典: {info['url']}）\n"

    combined_prompt += "\n最終的な回答は、簡潔で直接的であり、専門用語の説明を一貫した形で統合してください。"
    return combined_prompt

def generate_final_answer(answer, data, model):
    # Generate the final answer
    combined_prompt = create_combined_prompt(answer, data)
    response = model(
        messages=[
            {"role": "system", "content": "あなたは簡潔で直接的な回答を提供する専門家です。無駄な説明や前置きを避け、質問に対して即座に核心を突いた回答をします。"},
            {"role": "user", "content": combined_prompt}
        ]
    )
    return response.content
