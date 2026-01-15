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

## 📁 Struktur Folder
```text
.
├── chroma_db/          # Vector store (di-ignore git)
├── documents/          # Dokumen sumber (PDF, txt, dll)
├── app.py              # Entry point aplikasi
├── requirements.txt
├── .env                # Environment variables (di-ignore git)
├── .gitignore
└── README.md
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
