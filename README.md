GenAI RAG Assessment
====================

This project implements a Retrieval-Augmented Generation (RAG) pipeline with two retrieval strategies.
It demonstrates ingestion of textual data, embedding generation, semantic vector search, and benchmarking.

------------------------------------------------------------
Project Structure
------------------------------------------------------------
genai-rag-assessment/
│── embeddings.py        # Embedding logic using sentence-transformers
│── storage.py           # Vector DB setup (FAISS)
│── retrieval.py         # Retrieval strategies A & B
│── pipeline.py          # Orchestration class (data ingestion + retrieval)
│── tests/
│    └── test_pipeline.py # Pytest cases for embeddings and retrieval
│── retrieval_benchmark.md # Comparison report (Strategy A vs Strategy B)
│── README.md            # Documentation

------------------------------------------------------------
Setup Instructions
------------------------------------------------------------
1. Install Python
   - Ensure you have Python 3.10+ installed.
   - Command: python --version

2. Create Virtual Environment
   - Command: python -m venv venv

   Windows (PowerShell):
   Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
   venv\Scripts\Activate.ps1

   Windows (CMD):
   venv\Scripts\activate.bat

   Mac/Linux:
   source venv/bin/activate

3. Install Dependencies
   - Command: pip install sentence-transformers faiss-cpu pytest

------------------------------------------------------------
Usage Guide
------------------------------------------------------------
Step 1: Run Pipeline
   Command: python pipeline.py
   - Ingests dataset
   - Generates embeddings
   - Builds FAISS index
   - Runs queries
   - Saves results to retrieval_benchmark.md

Step 2: Run Tests
   Command: pytest
   or: pytest tests/

------------------------------------------------------------
Example Output
------------------------------------------------------------
Query: How does the system handle peak load?

Strategy A (Raw Vector Search):
- System scales horizontally using load balancers.
- Peak traffic managed with auto-scaling groups.
- Distributed queues handle high demand efficiently.

Strategy B (Query Expansion):
- System scales horizontally using load balancers.
- Distributed queues handle high demand efficiently.
- Peak traffic managed with auto-scaling groups.

------------------------------------------------------------
Documentation Notes
------------------------------------------------------------
- Similarity Metric: Cosine similarity is used because it measures semantic orientation rather than magnitude.
- Migration Plan: FAISS can be replaced with Vertex AI Matching Engine for production scalability.
  Embeddings can be generated using textembedding-gecko and stored in Matching Engine for high-performance retrieval.

------------------------------------------------------------
Deliverables
------------------------------------------------------------
- Modular Python code
- Pytest suite
- Benchmark comparison report (retrieval_benchmark.md)
- Clear documentation (README.md)
