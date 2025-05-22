import streamlit as st
from src.pdf_loader import load_and_split_pdf
from src.rag_chain import generate_answer
from src.memory import get_session_memory
from config.settings import EMBEDDING_MODEL, EMBEDDING_NAME
import os
from src.pdf_loader import load_and_split_pdf, generate_answer

# Page configuration
st.set_page_config(page_title="📄 PDF Chat Assistant", layout="wide")

# Sidebar: PDF upload
st.sidebar.title("📁 Upload PDFs")
uploaded_files = st.sidebar.file_uploader("Choose one or more PDFs", type="pdf", accept_multiple_files=True)

# App title
st.markdown("<h1 style='text-align: center;'>🤖 Chat with Your PDFs</h1>", unsafe_allow_html=True)

# Initialize session memory
memory = get_session_memory()

# Load PDFs and split
docs = None
if uploaded_files:
    docs = load_and_split_pdf(uploaded_files)
    st.sidebar.success(f"✅ Loaded and split {len(docs)} chunks.")

# Main content area
if docs:
    col1, col2, col3 = st.columns([1, 4, 1])  # Center the chat input
    with col2:
        st.markdown("### 💬 Ask a question")
        question = st.text_input("Type your question here:")

        if question:
            with st.spinner("🤔 Thinking..."):
                response, sources = generate_answer(question, docs, memory)

            st.markdown("### 🧠 Answer")
            st.success(response)

            with st.expander("📚 Source Chunks"):
                for i, source in enumerate(sources):
                    st.markdown(f"**{i+1}.** {source}")
else:
    st.markdown("<p style='text-align: center; color: grey;'>Upload PDFs from the sidebar to start chatting.</p>", unsafe_allow_html=True)
