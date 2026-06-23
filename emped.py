import time
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

# Importing our custom functions from Day 2
from load_docs import load_any_document
from split_docs import split_documents

def main():
    # 1. Ask the user for the file
    user_file_path = input("📂 Enter the path of the document to process:\n> ")
    
    # 2. Load and split the document
    docs = load_any_document(user_file_path)
    if not docs:
        return
        
    chunks = split_documents(docs, chunk_size=1000, chunk_overlap=200)
    if not chunks:
        print("❌ Error: No text chunks were generated.")
        return

    # 3. Initialize the Embedding Model (HuggingFace all-MiniLM-L6-v2)
    print("\n🧠 Downloading/Loading the Embedding Model (all-MiniLM-L6-v2)...")
    # Note: It might take a minute on the first run to download the model (~80MB)
    embeddings_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

    # 4. Show the Vector Shape (Trade-off observation from the plan)
    first_chunk_text = chunks[0].page_content
    sample_vector = embeddings_model.embed_query(first_chunk_text)
    print("\n--- Vector Shape Observation ---")
    print(f"🔢 The model turned the first chunk into a list of {len(sample_vector)} numbers!")
    print(f"Here are the first 5 numbers of this vector: {sample_vector[:5]}...")

    # 5. Store chunks in FAISS Database
    print("\n📦 Storing vectors into FAISS Database...")
    start_time = time.time()
    vector_store = FAISS.from_documents(chunks, embeddings_model)
    end_time = time.time()
    print(f"✅ Vectors stored successfully in {round(end_time - start_time, 2)} seconds!")

    # 6. Test Semantic Search
    print("\n" + "="*50)
    print("🔍 TEST SEMANTIC SEARCH")
    print("="*50)
    
    while True:
        query = input("\n❓ Ask a question to search the document (or type 'exit' to quit):\n> ")
        if query.lower() == 'exit':
            break
            
        print(f"⏳ Searching for the top 3 most relevant chunks for: '{query}'...")
        
        # Retrieve the top 3 chunks (k=3)
        search_start = time.time()
        results = vector_store.similarity_search(query, k=3)
        search_end = time.time()
        
        print(f"\n⚡ Search completed in {round(search_end - search_start, 3)} seconds.")
        print("\n🏆 TOP 3 CHUNKS FOUND:")
        for i, res in enumerate(results):
            print(f"\n--- Result [{i+1}] ---")
            print(res.page_content)
            print("-" * 40)

if __name__ == "__main__":
    main()