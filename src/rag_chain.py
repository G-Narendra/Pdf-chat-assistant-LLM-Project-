from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.chains import RetrievalQA
from langchain.llms import HuggingFaceHub
from langchain.schema import BaseRetriever  # ✅ Add this import
from config.settings import HUGGINGFACEHUB_API_TOKEN, EMBEDDING_NAME, LLM_MODEL_NAME

# Load embedding model
embedding = HuggingFaceEmbeddings(model_name=EMBEDDING_NAME)

def generate_answer(question, docs, memory):
    db = FAISS.from_documents(docs, embedding)
    retriever: BaseRetriever = db.as_retriever(search_type="similarity", search_kwargs={"k": 4})  # ✅ Add type hint
    llm = HuggingFaceHub(
    repo_id=LLM_MODEL_NAME,
    model_kwargs={"temperature": 0.7, "max_new_tokens": 256},
    huggingfacehub_api_token=HUGGINGFACEHUB_API_TOKEN,
    task="text-generation"  # Explicitly tell LangChain what the model does
    )
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=retriever,
        memory=memory
    )
    response = qa_chain.run(question)
    sources = [doc.page_content for doc in retriever.get_relevant_documents(question)]
    return response, sources
