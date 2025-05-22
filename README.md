🧠 PDF Chat Assistant – Chat with Your PDFs using LangChain, Hugging Face & Streamlit
Interact with your PDF documents using natural language! This beginner-friendly, fully local application leverages LangChain, Hugging Face, and Streamlit to let you upload one or more PDFs, ask contextual questions, and receive intelligent, grounded answers — with clear source references for transparency.

🚀 Key Features
📄 Multi-PDF Upload: Upload one or multiple PDF documents for context-aware Q&A.

✂️ Smart Chunking: Cleanly extracts and splits content using PyMuPDF for efficient embedding.

🧠 State-of-the-Art Embeddings: Powered by Hugging Face's Sentence Transformers.

📦 Fast Local Vector Search: Uses FAISS for fast similarity-based retrieval — fully offline.

🤖 LLM Integration: Answers generated via open-source models (e.g., Mistral-7B-Instruct) through Hugging Face Hub.

💬 Conversational Memory: Maintains dialogue history with LangChain memory for coherent interactions.

🗃️ Source Visibility: Displays PDF source context chunks for every answer (RAG-style UI).

🧠 Session Logging: Saves chat history to JSON for future reference.

🌐 Elegant Web UI: Built with Streamlit for an intuitive and clean chat experience.

🗂️ Project Structure
text
Copy
Edit
pdf_chat_assistant/
├── .env                  # 🔐 API keys and config (excluded from Git)
├── .gitignore            # 🚫 Files and folders to ignore
├── README.md             # 📘 Project documentation (this file)
├── requirements.txt      # 📦 Python dependencies
├── app.py                # 🚀 Streamlit app entry point
├── config/
│   └── settings.py       # ⚙️ Environment settings, keys, model configs
├── data/
│   └── uploads/          # 📄 Uploaded PDFs (runtime)
├── src/
│   ├── pdf_loader.py     # 📚 PDF text extractor and chunker
│   ├── rag_chain.py      # 🔍 RAG logic: retrieval + LLM generation
│   ├── memory.py         # 🧠 Conversational memory handler
│   └── utils.py          # 🛠️ Utility functions
├── vectorstore/
│   └── faiss_index/      # 🧬 Local vector index (FAISS)
└── chat_logs/
    └── chat_history.json # 💬 Saved conversations
⚙️ Installation & Setup
Follow these steps to get the app running locally:

1. Clone the Repository
bash
Copy
Edit
git clone https://github.com/your-username/pdf-chat-assistant.git
cd pdf_chat_assistant
2. Create a Virtual Environment
bash
Copy
Edit
python -m venv venv
# Activate (Windows)
venv\Scripts\activate
# OR (Linux/Mac)
source venv/bin/activate
3. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
4. Add Hugging Face API Token
Create a .env file and add your Hugging Face token:

bash
Copy
Edit
HUGGINGFACEHUB_API_TOKEN=your_token_here
Or in terminal (for temporary use):

bash
Copy
Edit
echo HUGGINGFACEHUB_API_TOKEN=your_token_here >> .env
🔑 You can get a token by logging into https://huggingface.co/settings/tokens

▶️ Running the App
Simply start the Streamlit application:

bash
Copy
Edit
streamlit run app.py
Visit http://localhost:8501 in your browser to start chatting with your PDFs!

💡 Example Questions You Can Ask
Once a PDF is uploaded, try questions like:

"What is the main idea of this document?"

"Summarize Section 3 for me."

"What are the steps outlined in the process?"

"Who is the intended audience?"

"Give me an example command mentioned."

📌 Requirements
Python 3.8+

Streamlit

LangChain

HuggingFace Transformers & Embeddings

FAISS

PyMuPDF (fitz)

📢 Contributing
Have ideas for improvement? Found a bug? Feel free to:

Open an issue

Submit a pull request

Suggest new features or model integrations

Contributions are warmly welcome! ❤️

📄 License
This project is licensed under the MIT License — use it freely in your own projects.

🌟 Acknowledgments
LangChain – Language model orchestration framework

Hugging Face – Open-source LLM and embedding APIs

Streamlit – Web app framework for ML apps

FAISS – Fast vector search engine

Ready to make your PDFs talk?
Clone, run, and start chatting! 🚀