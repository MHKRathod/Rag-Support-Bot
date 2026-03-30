# RAG-Based Q&A Support Bot

This project is a **Question & Answer support bot** built using **Retrieval-Augmented Generation (RAG)**.  
The bot answers user questions **only from the content of a crawled website**, ensuring grounded and non-hallucinated responses.

The project demonstrates the complete RAG workflow:
**crawling → cleaning → chunking → embeddings → vector database → retrieval → API**.

---

## 📌 Project Objective

To build a backend API that:
- Crawls a website
- Stores its content in a vector database
- Retrieves relevant content for a user query
- Returns answers strictly based on the crawled data

---

## 🌐 Website Used

- **FastAPI Official Documentation**
- URL: https://fastapi.tiangolo.com/

---

## 🧠 Architecture Overview

Website
↓
Crawler (requests + BeautifulSoup)
↓
Text Cleaning
↓
Chunking
↓
Embeddings (Sentence Transformers)
↓
Vector Database (ChromaDB - Persistent)
↓
Retriever
↓
FastAPI Endpoint (/ask)


---

## 🛠️ Tech Stack

- **Python 3.13**
- **FastAPI** – API framework
- **ChromaDB** – Vector database
- **sentence-transformers** – Local embedding generation
- **BeautifulSoup** – HTML parsing
- **Uvicorn** – ASGI server

---

## 📂 Project Structure
rag-support-bot/
│
├── app/
│ ├── crawler.py # Crawls website pages
│ ├── cleaner.py # Cleans raw text
│ ├── chunker.py # Splits text into chunks
│ ├── embedder.py # Generates & stores embeddings
│ ├── rag.py # Retrieval logic
│ └── main.py # FastAPI application
│
├── data/
│ ├── raw_pages/ # Crawled raw pages
│ └── cleaned/ # Cleaned text files
│
├── vectorstore/
│ └── chroma/ # Persistent ChromaDB data
│
├── venv/ # Python virtual environment
└── README.md


---

## ⚙️ Setup Instructions

### 1️⃣ Create & Activate Virtual Environment (Windows)

/```bash
python -m venv venv
venv\Scripts\activate


#Install Dependecies:

#pip install fastapi uvicorn chromadb sentence-transformers requests beautifulsoup4 python-dotenv


pip install fastapi uvicorn chromadb sentence-transformers requests beautifulsoup4 python-

## Limitations
- Answers depend on retrieved chunks
- Some irrelevant content may be returned
- Limited to ~30 crawled pages

## Future Improvements
- Better HTML cleaning
- Better ranking
- Larger LLM


📌 Conclusion

This project demonstrates a complete, production-style Retrieval-Augmented Generation pipeline, covering data ingestion, vector search, and API-based querying.
It is suitable for use cases such as documentation assistants, support bots, and internal knowledge systems.


Submission branch for RAG project.
