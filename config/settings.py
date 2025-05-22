import os
from dotenv import load_dotenv

load_dotenv()

EMBEDDING_NAME = "all-MiniLM-L6-v2"
EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"


HUGGINGFACEHUB_API_TOKEN = os.getenv("HUGGINGFACEHUB_API_TOKEN")
LLM_MODEL_NAME = "HuggingFaceH4/zephyr-7b-beta" # or any suitable model
