from langchain_text_splitters import RecursiveCharacterTextSplitter
# Import our custom function from load_docs.py
from load_docs import load_any_document 

def split_documents(documents, chunk_size=1000, chunk_overlap=200):
    print(f"\n⏳ Splitting text (chunk_size: {chunk_size}, chunk_overlap: {chunk_overlap})...")
    
    # Initialize the text splitter with desired parameters
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        length_function=len,
        is_separator_regex=False,
    )
    
    # Execute the split operation
    chunks = text_splitter.split_documents(documents)
    print(f"✅ Splitting successful! Resulted in {len(chunks)} chunks.")
    return chunks

if __name__ == "__main__":
    # Ask the user for the file path to process
    user_file_path = input("📂 Enter the path of the file you want to split:\n> ")
    
    docs = load_any_document(user_file_path)
    
    if docs:
        # Perform splitting using the default parameters from the 14-day plan
        chunks = split_documents(docs, chunk_size=1000, chunk_overlap=200)
        
        print("\n--- Preview of the first 3 chunks ---")
        # Loop through and print the first 3 chunks to verify overlap and size
        for i, chunk in enumerate(chunks[:3]):
            print(f"\n🧩 Chunk [{i+1}]:")
            print(chunk.page_content[:300]) # Print first 300 chars of each chunk
            print("-" * 40)