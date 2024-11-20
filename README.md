# InternProject
**Basic RAG**

nano.ipynb に対応

    初期のRAGシステムを作成し、Markdownファイルのタイトルでチャンクを分け、text-embedding-3-largeで埋め込みを行いました。距離による類似度を計算して検索し、得られた情報をgpt-4oに送って回答を生成しました。

**Advanced RAG**

cleaning.py, embedding.py, eval.py, main.py に対応
    
    初級RAGを基に、Markdownのデータ形式を再調整し、FAISSの検索方法を距離ベースの類似度からCosine類似度に変更しました。

    RAG Fusionを追加し、チャンクの並び順を再計算（Reciprocal Rank Fusion）しました。
    また、Googleを用いた補助検索を追加し、LLMでキーワードを抽出しました。

    RAGの評価指標（RAGAS、専門用語の使用頻度、読みやすさ、METEOR/BLEU、Precision@k、Recall@k）を調査しました。

    分かち書きにはsudachi-pyを使用しました。

## リポジトリ概要
今回はAzure OpenAIとLangChainなどのツールを使用して、RAGシステムを作成し、テキストに基づいてQA応答するチャットボットです。
### 各ツールの概要とReadMe
embedding.py 
- create_embeddings_modelとcreate_chat_model：Azure OpenAIのAPIを使用。
- create_vectorstore：ベクトルデータベースを保存。
- load_vectorstore：ローカルから保存済みのFAISSベクトルを読み込む。
- query_generator：入力されたクエリに対して、複数の類似クエリを生成。
- normalize_vectors：クエリのベクトルを正規化し、コサイン類似度を計算。
- rrf_retriever：RAG Fusionの実装。
- create_prompt：検索されたドキュメントとクエリを組み合わせてプロンプトを生成。
- generate_answer：OpenAIを使って答えを生成。

cleaning.py
- find_jp_md_files：すべての.jp.mdファイルを検索。
- extract_path：パスの元データを抽出。
- process_md_files：page_contentとmetadataを抽出して、Documentオブジェクトを作成。
- clean_html：正規表現を使用してHTMLタグを除去。
- chunk_md_files：タイトル（#, ##,...）ごとに文書を分割。

search.py
- GoogleSearchクラス
    - init：初期化。
    - fetech_links：クエリに関連するGoogleのリンクを取得。
    - fetech_content：特定のURLのWebページ内容を取得。
- SemanticSearcherクラス
    - init：初期化。
    - get_embedding：テキストに対して埋め込み表現を生成。
    - find_best_match：クエリに最も似た文書を返す。
- get_best_answer：クエリに最も関連するWebページの内容を見つけて返す。

eval.py
- filtered_keywords：キーワードリストをフィルタリング。
- get_ragas_score：RAGASスコアを計算。
- meteor_score：METEORスコアを計算。
- extract_technical_terms：入力テキストから専門用語を抽出。
- remove_special_terms：テキストのトークン化後、専門用語を削除。
- calculate_term_density：テキスト内の専門用語の割合を計算。
- create_combined_prompt：回答と専門用語の説明を組み合わせてプロンプトを作成。
- generate_final_answer：最終的な答えを生成。

nano.ipynb 
- Basic RAGの実装です。使用している関数は基本的に同じです。

### 説明
- データセットはcontentフォルダにあります。
- dataフォルダには、今回の分析用ExcelファイルとFAISSベクトルデータベースの保存場所があります。（vectordbはAdvanced RAG、vectordb_testはBasic RAGの保存場所です。）
