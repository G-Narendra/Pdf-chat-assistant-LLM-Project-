from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.chains import RetrievalQA
from langchain.llms import HuggingFaceHub
from langchain.prompts import PromptTemplate
from langchain.schema import BaseRetriever
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from typing import List
import tempfile

from config.settings import HUGGINGFACEHUB_API_TOKEN, EMBEDDING_NAME, LLM_MODEL_NAME

# Load embedding model
embedding = HuggingFaceEmbeddings(model_name=EMBEDDING_NAME)

# Custom concise prompt
prompt_template = """
You are a concise AI assistant. Answer the question using only the relevant information from the context below. Do not repeat the question. If the answer cannot be found, reply with "Sorry, I don't know."

Context:
{context}

Question: {question}
Answer:"""


prompt = PromptTemplate(template=prompt_template, input_variables=["context", "question"])


# ✅ Add this function
def load_and_split_pdf(uploaded_files) -> List:
    docs = []
    for uploaded_file in uploaded_files:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
            tmp_file.write(uploaded_file.read())
            tmp_file_path = tmp_file.name

        loader = PyPDFLoader(tmp_file_path)
        pdf_pages = loader.load()
        splitter = RecursiveCharacterTextSplitter(chunk_size=800, chunk_overlap=100)
        chunks = splitter.split_documents(pdf_pages)
        docs.extend(chunks)
    return docs


def generate_answer(question, docs, memory):
    db = FAISS.from_documents(docs, embedding)
    
    retriever: BaseRetriever = db.as_retriever(
        search_type="similarity",
        search_kwargs={"k": 3}
    )
    
    llm = HuggingFaceHub(
        repo_id=LLM_MODEL_NAME,
        model_kwargs={"temperature": 0.7, "max_new_tokens": 256},
        huggingfacehub_api_token=HUGGINGFACEHUB_API_TOKEN,
        task="text-generation"
    )

    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=retriever,
        memory=memory,
        chain_type_kwargs={"prompt": prompt}
    )

    response = qa_chain.run(question)
    sources = [doc.page_content for doc in retriever.get_relevant_documents(question)]
    return response.strip(), sources
