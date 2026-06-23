import os
from fastapi import FastAPI, UploadFile, File, HTTPException
from pydantic import BaseModel
from langchain_groq import ChatGroq
from langchain_classic.chains import RetrievalQA
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

from load_docs import load_any_document
from split_docs import split_documents

# 1. Fetch your API key from environment variables (Safer for GitHub)
api_key = os.getenv("GROQ_API_KEY")
if api_key:
    os.environ["GROQ_API_KEY"] = api_key

# 2. Create the application
app = FastAPI(title="RAG AI Backend", description="My First AI API")

# 3. Server memory variables (Global variables to store state)
vector_store = None
qa_chain = None
llm = ChatGroq(model_name="llama-3.3-70b-versatile", temperature=0)
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

# 4. Define the required data model for requests
class QuestionRequest(BaseModel):
    question: str

@app.get("/health")
def health_check():
    return {"status": "ok", "message": "Server is healthy!"}

@app.post("/upload")
async def upload_document(file: UploadFile = File(...)):
    global vector_store, qa_chain
    
    # Save the uploaded file temporarily
    temp_file_path = f"temp_{file.filename}"
    with open(temp_file_path, "wb") as f:
        f.write(await file.read())
        
    try:
        # Process the file
        docs = load_any_document(temp_file_path)
        if not docs:
            raise HTTPException(status_code=400, detail="Could not read document")
            
        chunks = split_documents(docs, chunk_size=1000, chunk_overlap=200)
        vector_store = FAISS.from_documents(chunks, embeddings)
        
        qa_chain = RetrievalQA.from_chain_type(
            llm=llm,
            chain_type="stuff",
            retriever=vector_store.as_retriever(search_kwargs={"k": 3}),
            return_source_documents=True
        )
        os.remove(temp_file_path) # Delete the temporary file after processing
        return {"message": f"Success! Processed {len(chunks)} chunks."}
    
    except Exception as e:
        if os.path.exists(temp_file_path):
            os.remove(temp_file_path)
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/ask")
def ask_question(request: QuestionRequest):
    global qa_chain
    if not qa_chain:
        raise HTTPException(status_code=400, detail="Please upload a document first.")
        
    # Fetch the answer
    result = qa_chain.invoke({"query": request.question})
    sources = [doc.page_content[:200] for doc in result["source_documents"]]
    
    return {"answer": result["result"], "sources": sources}