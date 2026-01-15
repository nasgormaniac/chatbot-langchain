# 📄 Chatbot LangChain

## 📌 Deskripsi Project

Project ini merupakan aplikasi berbasis **LLM + RAG (Retrieval-Augmented Generation)** yang menggunakan vector database untuk pencarian konteks dan LLM berbasis API untuk menghasilkan jawaban.

---

## 🧱 Tech Stack
- Python
- LangChain
- Groq (LLM API)
- HuggingFace Embeddings
- ChromaDB
- Gradio
- python-dotenv

---

## How to Use
### Clone the Project

```bash
git clone https://github.com/nasgormaniac/chatbot-langchain.git
cd chatbot-langchain
```

### Install Requirements
```bash
pip install -r requirements.txt
```

### Run the Program
```bash
python ingest_db.py
```
Lalu baru jalankan:
```bash
python chatbot.py
```
Anda bisa menambahkan file pdf ke folder documents sebagai bahan untuk RAG

---

## 📁 Struktur Folder
```text
.
├── chroma_db/          # Vector store
├── documents/          # Dokumen sumber (PDF, txt, dll)
├── ingest_db.py        # Ingest data ke dalam DB
├── chatbot.py          # Aplikasi chatbot
├── requirements.txt
├── .env                # Environment variables
├── .gitignore
└── README.md
