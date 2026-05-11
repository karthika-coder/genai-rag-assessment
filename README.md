# GenAI RAG Vector Search Assessment

This project implements a **Context-Aware Retrieval Engine** using a local Retrieval-Augmented Generation (RAG) pipeline.  
It demonstrates ingestion of textual data, embedding generation, semantic vector search, and benchmarking of two retrieval strategies:

- **Strategy A (Raw Vector Search)**: Direct embedding-based similarity search.
- **Strategy B (AI-Enhanced Retrieval)**: Query expansion using a mocked model before embedding.

---

## 📂 Project Structure
genai-rag-assessment/
│── embeddings.py        # Embedding logic using sentence-transformers
│── storage.py           # Vector DB setup (FAISS)
│── retrieval.py         # Retrieval strategies A & B
│── pipeline.py          # Orchestration class (data ingestion + retrieval)
│── tests/
│    └── test_pipeline.py # Pytest cases for embeddings, retrieval, mocking
│── retrieval_benchmark.md # Comparison report (Strategy A vs B)
│── README.md            # Setup + documentation