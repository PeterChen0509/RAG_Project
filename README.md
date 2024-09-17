# Sony_InternProj
**初级RAG**\
    `nano.ipynb`
    做了初始的RAG系统，按Markdown文件的Title进行分块，用text-embedding-3-large做嵌入，直接算距离做相似度，检索到的信息送入gpt-4o生成答案

**高级RAG**\
    在初级的基础上，重新对Markdown调整数据格式，对 chunk 分块的文本做数据清洗，对FAISS的检索方式从距离相似度修改为Cosine相似度
    添加RAG Fusion，重新计算chunk排序(Reciprocal Rank Fusion)
    添加Google辅助检索，用LLM抽取关键字，调研了RAG的评价指标(RAGAS, 专有名词的使用频率，読みやすさ，METEOR/BLEU, Precision@k, Recall@k)
    分词用的是sudachi-py

