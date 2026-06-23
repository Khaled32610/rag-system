# 🧠 RAG Document Q&A System

An intelligent, fully containerized Retrieval-Augmented Generation (RAG) backend system. This API allows users to upload documents and ask natural language questions about their content, receiving highly accurate answers grounded in the provided text to eliminate AI hallucination.

## 🚀 Key Features
- **Document Processing:** Instantly uploads, parses, and chunks documents (PDF, DOCX, TXT).
- **Semantic Search:** Utilizes HuggingFace embeddings and FAISS vector database for lightning-fast, context-aware retrieval.
- **Advanced AI Reasoning:** Powered by Groq's blazing-fast inference and the Llama-3 70B model.
- **Source Tracking:** Returns exact text snippets (sources) used to generate the answer for fact-checking and transparency.
- **Containerized:** Fully packaged with Docker for seamless deployment and execution across any environment.

## 🛠️ Tech Stack
- **Framework:** FastAPI, Python 3.11
- **AI & Orchestration:** LangChain, Groq API (`llama-3.3-70b-versatile`)
- **Embeddings:** HuggingFace (`all-MiniLM-L6-v2`), Sentence-Transformers
- **Vector Store:** FAISS
- **Deployment:** Docker, Uvicorn

## ⚙️ Getting Started

### Prerequisites
- Docker Desktop installed and running.
- A free API key from [Groq](https://console.groq.com/).

### Installation & Running (Docker)
1. **Clone the repository:**
   ```bash
   git clone [https://github.com/Khaled32610/rag-system.git](https://github.com/Khaled32610/rag-system.git)
   cd rag-system