import os
import time
from langchain_groq import ChatGroq
from langchain_classic.chains import RetrievalQA
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

# Import our functions from previous days
from load_docs import load_any_document
from split_docs import split_documents

def main():
    # 1. Setup Groq API Key
    print("="*50)
    api_key = input("🔑 Enter your Groq API Key (starts with gsk_):\n> ").strip()
    os.environ["GROQ_API_KEY"] = api_key

    # Initialize the LLM (Using Llama3 with temperature 0 for factual accuracy)
    llm = ChatGroq(model_name="llama-3.3-70b-versatile", temperature=0)

    # 2. Hallucination Test (Asking the model without providing the document)
    print("\n" + "="*50)
    print("🧪 TEST 1: RAW QUESTION (Observe Hallucination)")
    print("="*50)
    raw_question = "What is the main topic of the document I have on my computer?"
    print(f"❓ Question: {raw_question}")
    print("⏳ Asking LLM without context...")
    raw_response = llm.invoke(raw_question)
    print(f"\n🤖 LLM Answer: {raw_response.content}")
    print("*(Notice how it apologizes or guesses because it can't see your file!)*\n")

    input("Press Enter to load your document and give it context...")

    # 3. Build RAG System (Load -> Split -> Store -> Retrieve)
    user_file_path = input("\n📂 Enter the path of the document to process:\n> ")
    docs = load_any_document(user_file_path)
    if not docs: return
        
    chunks = split_documents(docs, chunk_size=1000, chunk_overlap=200)
    if not chunks: return

    print("\n🧠 Loading Embeddings & Creating FAISS Vector Store...")
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    vector_store = FAISS.from_documents(chunks, embeddings)

    # 4. The real magic: Building the RetrievalQA Chain
    print("\n🔗 Building the RetrievalQA Chain...")
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff", # Stuffs all retrieved chunks into the prompt
        retriever=vector_store.as_retriever(search_kwargs={"k": 3}), # Retrieve the top 3 chunks
        return_source_documents=True # Very important: Return sources to verify the answer
    )
    print("✅ System is READY!")

    # 5. Test the System (Questioning with source citation)
    print("\n" + "="*50)
    print("🎯 TEST 2: RAG SYSTEM (Ask 5 Questions)")
    print("="*50)
    
    question_count = 0
    while question_count < 5:
        query = input(f"\n❓ Question [{question_count+1}/5] (or 'exit'):\n> ")
        if query.lower() == 'exit': break
            
        print("⏳ Thinking and searching...")
        start_time = time.time()
        
        # Run the chain
        result = qa_chain.invoke({"query": query})
        
        end_time = time.time()
        
        # Print the answer
        print(f"\n💡 Answer (in {round(end_time - start_time, 2)}s):")
        print(result["result"])
        
        # Print the sources
        print("\n📚 Sources used for this answer:")
        for i, doc in enumerate(result["source_documents"]):
            print(f"  - Source {i+1}: {doc.page_content[:150]}...") # Print only the first 150 characters of the source
            
        question_count += 1

if __name__ == "__main__":
    main()