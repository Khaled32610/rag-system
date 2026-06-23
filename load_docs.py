import os
from langchain_community.document_loaders import PyPDFLoader, TextLoader, Docx2txtLoader

def load_any_document(file_path):
    # Remove quotes if the user used drag-and-drop in the terminal
    file_path = file_path.strip("\"'") 
    
    # Check if the file actually exists
    if not os.path.exists(file_path):
        print(f"❌ Error: File not found at this path: {file_path}")
        return None

    print(f"⏳ Loading file: {file_path}...")
    
    # Extract file extension to determine the appropriate loader
    file_extension = os.path.splitext(file_path)[1].lower()
    
    try:
        if file_extension == '.pdf':
            loader = PyPDFLoader(file_path)
        elif file_extension == '.txt':
            loader = TextLoader(file_path, encoding='utf-8')
        elif file_extension == '.docx':
            loader = Docx2txtLoader(file_path)
        else:
            print(f"❌ Error: Unsupported file format '{file_extension}'.")
            return None
        
        # Load the document content
        documents = loader.load()
        print(f"✅ File loaded successfully! It contains {len(documents)} page(s)/part(s).")
        return documents
        
    except Exception as e:
        print(f"❌ An error occurred while trying to read the file: {e}")
        return None

if __name__ == "__main__":
    # Ask the user to input the file path
    user_file_path = input("📂 Enter the path of the file you want to read:\n> ")
    
    docs = load_any_document(user_file_path)
    
    if docs:
        print("\n--- Preview of the beginning (Raw Text) ---")
        # Print the first 500 characters of the first page to preview
        print(docs[0].page_content[:500])