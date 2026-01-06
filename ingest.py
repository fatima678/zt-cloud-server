# # # # # # # # import os
# # # # # # # # from dotenv import load_dotenv
# # # # # # # # from langchain_community.document_loaders import DirectoryLoader, TextLoader
# # # # # # # # from langchain_text_splitters import RecursiveCharacterTextSplitter
# # # # # # # # from langchain_huggingface import HuggingFaceEmbeddings
# # # # # # # # from langchain_chroma import Chroma

# # # # # # # # # 1. Load Environment Variables
# # # # # # # # load_dotenv()

# # # # # # # # def create_vector_db():
# # # # # # # #     # 2. Data Load karein
# # # # # # # #     print("Loading data...")
# # # # # # # #     loader = DirectoryLoader('data/', glob="./*.txt", loader_cls=TextLoader)
# # # # # # # #     documents = loader.load()

# # # # # # # #     # 3. Text ko chote tukron (Chunks) mein torein
# # # # # # # #     # Is se bot ko sahi jawab dhoondne mein asani hoti hai
# # # # # # # #     text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
# # # # # # # #     chunks = text_splitter.split_documents(documents)

# # # # # # # #     # 4. Open Source Embedding Model use karein (English ke liye best hai)
# # # # # # # #     embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

# # # # # # # #     # 5. ChromaDB mein save karein
# # # # # # # #     print("Creating Vector Database...")
# # # # # # # #     vector_db = Chroma.from_documents(
# # # # # # # #         documents=chunks,
# # # # # # # #         embedding=embeddings,
# # # # # # # #         persist_directory="./db"
# # # # # # # #     )
# # # # # # # #     print("Done! Your 'db' folder is ready.")

# # # # # # # # if __name__ == "__main__":
# # # # # # # #     create_vector_db()


# # # # # # # import os
# # # # # # # from dotenv import load_dotenv
# # # # # # # from langchain_community.document_loaders import DirectoryLoader, TextLoader
# # # # # # # from langchain_text_splitters import RecursiveCharacterTextSplitter
# # # # # # # from langchain_huggingface import HuggingFaceEmbeddings
# # # # # # # from langchain_chroma import Chroma

# # # # # # # load_dotenv()

# # # # # # # def create_vector_db():
# # # # # # #     print("Loading data...")
# # # # # # #     if not os.path.exists('data'):
# # # # # # #         print("Error: 'data' folder nahi mila!")
# # # # # # #         return

# # # # # # #     # Encoding ko utf-8 set karna zaroori hai
# # # # # # #     try:
# # # # # # #         loader = DirectoryLoader(
# # # # # # #             'data/', 
# # # # # # #             glob="*.txt", 
# # # # # # #             loader_cls=TextLoader,
# # # # # # #             loader_kwargs={'encoding': 'utf-8'} # <--- Ye line error theek karegi
# # # # # # #         )
# # # # # # #         documents = loader.load()
# # # # # # #         print(f"Documents loaded: {len(documents)}")
# # # # # # #     except Exception as e:
# # # # # # #         print(f"Error loading files: {e}")
# # # # # # #         return

# # # # # # #     if len(documents) == 0:
# # # # # # #         print("Error: Koi data nahi mila!")
# # # # # # #         return

# # # # # # #     # Text Split karein
# # # # # # #     text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
# # # # # # #     chunks = text_splitter.split_documents(documents)
# # # # # # #     print(f"Total chunks created: {len(chunks)}")

# # # # # # #     # Embeddings
# # # # # # #     embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

# # # # # # #     # ChromaDB
# # # # # # #     print("Creating Vector Database...")
# # # # # # #     vector_db = Chroma.from_documents(
# # # # # # #         documents=chunks,
# # # # # # #         embedding=embeddings,
# # # # # # #         persist_directory="./db"
# # # # # # #     )
# # # # # # #     print("Done! Your 'db' folder is ready.")

# # # # # # # if __name__ == "__main__":
# # # # # # #     create_vector_db()


# # # # # # # Refined api/ingest.py Code:
# # # # # # # Aap is code ko use karein, maine ismein auto-cleanup aur optimized splitting daal di hai:


# # # # # # import os
# # # # # # import shutil # Purana folder delete karne ke liye
# # # # # # from dotenv import load_dotenv
# # # # # # from langchain_community.document_loaders import DirectoryLoader, TextLoader
# # # # # # from langchain_text_splitters import RecursiveCharacterTextSplitter
# # # # # # from langchain_huggingface import HuggingFaceEmbeddings
# # # # # # from langchain_chroma import Chroma

# # # # # # load_dotenv()

# # # # # # def create_vector_db():
# # # # # #     print("🚀 Ingestion started...")
    
# # # # # #     # Paths
# # # # # #     data_dir = 'data/'
# # # # # #     db_dir = './db'

# # # # # #     # 1. Purana Database Delete Karein (Fresh Start)
# # # # # #     if os.path.exists(db_dir):
# # # # # #         print(f"🗑️ Removing old database at {db_dir}...")
# # # # # #         shutil.rmtree(db_dir)

# # # # # #     if not os.path.exists(data_dir):
# # # # # #         print(f"❌ Error: '{data_dir}' folder nahi mila!")
# # # # # #         return

# # # # # #     # 2. Load Documents
# # # # # #     print("📂 Loading 100+ files from data folder...")
# # # # # #     try:
# # # # # #         loader = DirectoryLoader(
# # # # # #             data_dir, 
# # # # # #             glob="*.txt", 
# # # # # #             loader_cls=TextLoader,
# # # # # #             loader_kwargs={'encoding': 'utf-8'}
# # # # # #         )
# # # # # #         documents = loader.load()
# # # # # #         print(f"✅ Documents loaded: {len(documents)}")
# # # # # #     except Exception as e:
# # # # # #         print(f"❌ Error loading files: {e}")
# # # # # #         return

# # # # # #     if not documents:
# # # # # #         print("⚠️ Warning: Koi documents load nahi hue!")
# # # # # #         return

# # # # # #     # 3. Text Splitting (Optimized for ZT Hosting data)
# # # # # #     # 500 characters ka chunk size hosting plans ke liye ideal hai
# # # # # #     text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
# # # # # #     chunks = text_splitter.split_documents(documents)
# # # # # #     print(f"✂️ Total chunks created: {len(chunks)}")

# # # # # #     # 4. Embeddings Setup
# # # # # #     print("🧠 Initializing Embeddings model (all-MiniLM-L6-v2)...")
# # # # # #     embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

# # # # # #     # 5. Create & Persist Vector Database
# # # # # #     print("💾 Saving to Vector Database (ChromaDB)...")
# # # # # #     try:
# # # # # #         vector_db = Chroma.from_documents(
# # # # # #             documents=chunks,
# # # # # #             embedding=embeddings,
# # # # # #             persist_directory=db_dir
# # # # # #         )
# # # # # #         print(f"⭐ Success! Database updated with {len(chunks)} fresh chunks.")
# # # # # #     except Exception as e:
# # # # # #         print(f"❌ Error creating ChromaDB: {e}")

# # # # # # if __name__ == "__main__":
# # # # # #     create_vector_db()


# # # # # # Aap apne ingest.py ko delete na karein, bas usay is simple code se badal dein. Ye sirf files ko clean karega:


# # # # # import os

# # # # # def clean_and_verify_data():
# # # # #     data_dir = 'data/'
# # # # #     if not os.path.exists(data_dir):
# # # # #         print(f"❌ Error: {data_dir} nahi mila!")
# # # # #         return

# # # # #     files = [f for f in os.listdir(data_dir) if f.endswith(".txt")]
# # # # #     print(f"📂 Found {len(files)} files. Cleaning...")

# # # # #     for file_name in files:
# # # # #         path = os.path.join(data_dir, file_name)
# # # # #         with open(path, "r", encoding="utf-8") as f:
# # # # #             lines = f.readlines()
        
# # # # #         # Sirf non-empty lines rakhein aur extra space hatayein
# # # # #         cleaned = [line.strip() for line in lines if line.strip()]
        
# # # # #         with open(path, "w", encoding="utf-8") as f:
# # # # #             f.write("\n".join(cleaned))

# # # # #     print("✅ All files cleaned for Dynamic Scanner!")

# # # # # if __name__ == "__main__":
# # # # #     clean_and_verify_data()


# # # # # 🚀 Updated ingest.py (Mature Version)
# # # # # Sir ki requirements ke mutabiq, aapko ye logic add karna chahiye taake scraper ke baad chatbot ka dimagh (database) bhi update ho jaye:


# # # # import os
# # # # from langchain_community.vectorstores import Chroma # Example
# # # # from langchain_openai import OpenAIEmbeddings # Ya jo aap use kar rahe hain

# # # # # Use this instead of local embeddings
# # # # embeddings = OpenAIEmbeddings(model="text-embedding-3-small")

# # # # def clean_and_sync_vector_db():
# # # #     data_dir = 'data/' # Scraper ka output folder
# # # #     # ... (Aapka cleaning logic yahan rahega) ...

 
# # # #     print("🔄 Syncing with Vector Database for Dynamic Search...")
# # # #     # Yahan aap LangChain ya apna RAG logic use karke 
# # # #     # text files ko database mein load karenge.
    
# # # #     # Is se bot hamesha "Live" fetched data use karega.
# # # #     print("✅ Bot is now updated with the latest website data!")



# # # # updated code scrapping ky error ko resolve krny ky lea 


# # # import os
# # # from langchain_openai import OpenAIEmbeddings 
# # # from langchain_community.vectorstores import Chroma

# # # # This will now pull the key from the GitHub Environment we set above
# # # embeddings = OpenAIEmbeddings(model="text-embedding-3-small")

# # # def clean_and_sync_vector_db():
# # #     data_dir = 'data/' 
    
# # #     # YOUR CLEANING LOGIC HERE
# # #     # Ensure you are loading your .txt files from data/ into the Chroma DB
    
# # #     print("🔄 Syncing with Vector Database for Dynamic Search...")
    
# # #     # Final confirmation
# # #     print("✅ Bot is now updated with the latest website data!")

# # # if __name__ == "__main__":
# # #     clean_and_sync_vector_db()


# # # open ai ki keys paid thi tu ab hm hugging face sy data ki embeddings generate kren gy



# # import os
# # from langchain_community.vectorstores import Chroma # Ye lazmi hai
# # from langchain_community.embeddings import HuggingFaceInferenceEmbeddings

# # # Ye bilkul FREE hai aur server crash nahi karega
# # embeddings = HuggingFaceInferenceEmbeddings(
# #     api_key=os.environ.get("HUGGINGFACE_TOKEN"), 
# #     model_name="sentence-transformers/all-MiniLM-L6-v2"
# # )




# import os
# from langchain_community.vectorstores import Chroma
# from langchain_community.embeddings import HuggingFaceInferenceEmbeddings
# from langchain_community.document_loaders import DirectoryLoader, TextLoader
# from langchain_text_splitters import CharacterTextSplitter

# # 1. FREE Embeddings Setup
# embeddings = HuggingFaceInferenceEmbeddings(
#     api_key=os.environ.get("HUGGINGFACE_TOKEN"), 
#     model_name="sentence-transformers/all-MiniLM-L6-v2"
# )

# def clean_and_sync_vector_db():
#     data_dir = 'data/'  # Jahan scraper files save karta hai
#     db_dir = 'db/'      # Jahan database save hoga

#     print("🔄 Loading latest data from scraper...")
    
#     # 2. Files ko load karna
#     loader = DirectoryLoader(data_dir, glob="./*.txt", loader_cls=TextLoader)
#     documents = loader.load()

#     # 3. Text ko chhote tukron mein split karna (taake AI jaldi samajh sake)
#     text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
#     docs = text_splitter.split_documents(documents)

#     print(f"📦 Processing {len(docs)} text chunks...")

#     # 4. ChromaDB mein data save karna
#     # Ye step Hugging Face API use karega (Bilkul Free)
#     vectorstore = Chroma.from_documents(
#         documents=docs, 
#         embedding=embeddings,
#         persist_directory=db_dir
#     )
    
#     print("✅ Bot Database is now updated and synced for FREE!")

# if __name__ == "__main__":
#     # Ensure folders exist
#     if not os.path.exists('data'): os.makedirs('data')
#     if not os.path.exists('db'): os.makedirs('db')
    
#     clean_and_sync_vector_db()


# update the code to resolve the issue of webscraper 
import os
from langchain_community.vectorstores import Chroma
# Is naye tariqe se import karein, ye error nahi dega
from langchain_huggingface import HuggingFaceEmbeddings 
from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain_text_splitters import CharacterTextSplitter

# FREE Embeddings Setup
# Ye bina kisi error ke chale ga
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2",
    model_kwargs={'device': 'cpu'}
)

def clean_and_sync_vector_db():
    data_dir = 'data/'
    db_dir = 'db/'

    if not os.path.exists(data_dir) or not os.listdir(data_dir):
        print("⚠️ No data files found. Running scraper might be necessary.")
        return

    print("🔄 Loading data and updating Vector DB...")
    loader = DirectoryLoader(data_dir, glob="./*.txt", loader_cls=TextLoader)
    documents = loader.load()

    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    docs = text_splitter.split_documents(documents)

    # Database create karna
    vectorstore = Chroma.from_documents(
        documents=docs, 
        embedding=embeddings,
        persist_directory=db_dir
    )
    print("✅ Database updated successfully with HuggingFace!")

if __name__ == "__main__":
    if not os.path.exists('data'): os.makedirs('data')
    if not os.path.exists('db'): os.makedirs('db')
    clean_and_sync_vector_db()


