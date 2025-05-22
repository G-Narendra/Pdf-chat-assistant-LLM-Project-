import os

def ensure_directories():
    os.makedirs("data/uploads", exist_ok=True)
    os.makedirs("vectorstore/faiss_index", exist_ok=True)
    os.makedirs("chat_logs", exist_ok=True)