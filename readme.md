# 🧠 RAG Document Q&A System

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python\&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-009688?logo=fastapi)
![LangChain](https://img.shields.io/badge/LangChain-RAG-green)
![FAISS](https://img.shields.io/badge/FAISS-VectorDB-orange)
![Docker](https://img.shields.io/badge/Docker-Containerized-2496ED?logo=docker)

A production-ready Retrieval-Augmented Generation (RAG) system that combines semantic search, vector databases, and Large Language Models (LLMs) to deliver accurate, source-grounded answers from user-provided documents.

Built with FastAPI, LangChain, FAISS, and Groq's Llama 3, the system enables intelligent document understanding while minimizing hallucinations through context-aware retrieval.

---

## 🚀 Features

* Upload and process PDF, DOCX, and TXT files
* Automatic document chunking
* Semantic search using vector embeddings
* Retrieval-Augmented Generation (RAG)
* Groq-powered Llama 3 inference
* Source-aware responses for transparency
* FastAPI REST API
* Dockerized deployment

---

## 🏗️ How It Works

```text
Document Upload
      ↓
Document Parsing
      ↓
Text Chunking
      ↓
Embeddings Generation
      ↓
FAISS Vector Store
      ↓
Similarity Search
      ↓
Relevant Context Retrieval
      ↓
Groq Llama 3
      ↓
Answer + Sources
```

---

## 🛠️ Tech Stack

| Category         | Technology         |
| ---------------- | ------------------ |
| Backend          | FastAPI, Uvicorn   |
| AI Framework     | LangChain          |
| LLM              | Groq Llama 3.3 70B |
| Embeddings       | all-MiniLM-L6-v2   |
| Vector Database  | FAISS              |
| Containerization | Docker             |
| Language         | Python 3.11        |

---

## 📦 Installation

### Clone Repository

```bash
git clone https://github.com/Khaled32610/rag-system.git
cd rag-system
```

### Create Virtual Environment

```bash
python -m venv venv
```

Windows:

```bash
venv\Scripts\activate
```

Linux/macOS:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure Environment Variables

Create a `.env` file:

```env
GROQ_API_KEY=your_api_key_here
```

### Run Server

```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

---

## 🐳 Docker Deployment

Build the image:

```bash
docker build -t rag-system .
```

Run the container:

```bash
docker run -p 8000:8000 --env-file .env rag-system
```

---

## 📡 API Endpoints

| Method | Endpoint  | Description                            |
| ------ | --------- | -------------------------------------- |
| GET    | `/health` | Health check                           |
| POST   | `/upload` | Upload and index a document            |
| POST   | `/ask`    | Ask questions about uploaded documents |

---

## 💡 Example Request

```json
{
  "question": "What are the key features of the system?"
}
```

### Example Response

```json
{
  "answer": "The system supports document upload, semantic retrieval, and source-grounded question answering.",
  "sources": [
    "Relevant document chunk 1",
    "Relevant document chunk 2"
  ]
}
```

---

## 📖 API Documentation

After running the server:

```text
http://localhost:8000/docs
```

---

## 🎯 Challenges Solved

This project addresses several common challenges in AI-powered question-answering systems:

* **Reducing Hallucinations:** Answers are generated using only the most relevant retrieved document context instead of relying solely on the LLM's internal knowledge.
* **Efficient Information Retrieval:** FAISS enables fast semantic similarity search even when working with large documents.
* **Explainable Responses:** The API returns the source chunks used to generate each answer, improving transparency and trust.
* **Scalable Architecture:** The system is modular and containerized, making deployment and future extensions straightforward.
* **Production-Ready Workflow:** Combines document ingestion, vector indexing, retrieval, and answer generation into a complete end-to-end pipeline.

### Key Learning Outcomes

Through this project, the following concepts were implemented and explored:

* Retrieval-Augmented Generation (RAG)
* Vector Databases and Similarity Search
* Embedding Models and Semantic Retrieval
* LangChain Orchestration
* FastAPI Backend Development
* Docker-Based Deployment
* LLM Integration using Groq APIs

---

## 🔮 Future Improvements

* Multi-document support
* Authentication & user management
* Chat history memory
* Hybrid Search (BM25 + Vector Search)
* ChromaDB integration
* Streaming responses
* React/Next.js frontend


