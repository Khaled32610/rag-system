# 🧠 RAG Document Q&A System

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.104.1-009688?logo=fastapi&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-Containerized-2496ED?logo=docker&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-Integration-green)

A production-ready **Retrieval-Augmented Generation (RAG)** system built with FastAPI. This backend API allows users to upload documents (PDF, TXT, DOCX), processes them into vector embeddings, and leverages Groq's blazing-fast Llama-3 model to answer questions based *strictly* on the document's context, eliminating AI hallucination.

---

## 🚀 Key Features

* **Intelligent Document Processing:** Instantly parses and chunks large documents.
* **Semantic Search:** Uses HuggingFace (`all-MiniLM-L6-v2`) and FAISS for highly accurate context retrieval.
* **Ultra-Fast Inference:** Powered by Groq's `llama-3.3-70b-versatile` model.
* **Source Tracking:** Returns the exact text snippets used to generate the answer for maximum transparency.
* **Fully Containerized:** Packaged with Docker for seamless, isolated deployment.

---

## 🛠️ Technology Stack

* **Backend:** FastAPI, Uvicorn, Python
* **AI & Orchestration:** LangChain, Groq API
* **Vector Database:** FAISS (Facebook AI Similarity Search)
* **Embeddings:** Sentence-Transformers (HuggingFace)
* **DevOps:** Docker

---

## ⚙️ Setup Instructions

You can run this project either locally using a Python virtual environment or securely via Docker.

### Prerequisites
* Python 3.11 or higher (if running locally)
* Docker Desktop (if running via Docker)
* A free API key from [Groq](https://console.groq.com/)

---

### Option A: Local Setup (Virtual Environment)

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/Khaled32610/rag-system.git](https://github.com/Khaled32610/rag-system.git)
   cd rag-system
Create and activate a virtual environment:Bash# On Windows:
python -m venv venv
venv\Scripts\activate

# On macOS/Linux:
python3 -m venv venv
source venv/bin/activate
Install the dependencies:Bashpip install -r requirements.txt
Set Up Credentials:Create a .env file in the root directory and add your Groq API key:Code snippetGROQ_API_KEY=gsk_your_api_key_here
Run the FastAPI Server:Bashuvicorn main:app --host 0.0.0.0 --port 8000 --reload
Option B: Docker SetupThe easiest way to deploy this project in an isolated environment.Clone the repository:Bashgit clone [https://github.com/Khaled32610/rag-system.git](https://github.com/Khaled32610/rag-system.git)
cd rag-system
Set Up Credentials:Create a .env file in the root directory and add your Groq API key:Code snippetGROQ_API_KEY=gsk_your_api_key_here
Build & Run the Container:Bash# Build the Docker image
docker build -t rag-system .

# Run the container mapping port 8000
docker run -p 8000:8000 --env-file .env rag-system
📡 API EndpointsOnce the server is running, visit the interactive Swagger UI at:👉 http://localhost:8000/docsMethodEndpointDescriptionGET/healthChecks if the API is running and healthy.POST/uploadUploads a document, chunks it, and updates the FAISS vector store.POST/askAccepts a JSON payload {"question": "..."} and returns the AI answer with sources.👨‍💻 AuthorKhaled Taha Full-Stack & AI Enthusiast | Building intelligent, containerized solutions.