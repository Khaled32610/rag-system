import time
from langchain_huggingface import HuggingFaceEmbeddings
# Import Chroma instead of FAISS
from langchain_community.vectorstores import Chroma

from load_docs import load_any_document
from split_docs import split_documents

def main():
    user_file_path = input("📂 Enter the path of the document to process:\n> ")
    docs = load_any_document(user_file_path)
    if not docs:
        return
        
    chunks = split_documents(docs, chunk_size=1000, chunk_overlap=200)
    if not chunks:
        return

    print("\n🧠 Loading Embedding Model (all-MiniLM-L6-v2)...")
    embeddings_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

    # Store vectors in ChromaDB and calculate elapsed time
    print("\n📦 Storing vectors into ChromaDB...")
    start_time = time.time()
    vector_store = Chroma.from_documents(documents=chunks, embedding=embeddings_model)
    end_time = time.time()
    print(f"✅ Vectors stored in ChromaDB in {round(end_time - start_time, 2)} seconds!")

    print("\n" + "="*50)
    print("🔍 TEST SEMANTIC SEARCH (ChromaDB)")
    print("="*50)
    
    while True:
        query = input("\n❓ Ask a question (or type 'exit' to quit):\n> ")
        if query.lower() == 'exit':
            break
            
        search_start = time.time()
        # The search implementation remains exactly the same!
        results = vector_store.similarity_search(query, k=3)
        search_end = time.time()
        
        print(f"\n⚡ Search completed in {round(search_end - search_start, 3)} seconds.")
        for i, res in enumerate(results):
            print(f"\n--- Result [{i+1}] ---")
            print(res.page_content)
            print("-" * 40)

if __name__ == "__main__":
    main()