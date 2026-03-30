from fastapi import FastAPI
from pydantic import BaseModel

import app.crawler as crawler 
from app.rag import answer_question
from app.crawler import crawl
from app.cleaner import clean_all
from app.embedder import embed_all

app = FastAPI(title="RAG Q&A Support Bot")

# -------------------------------
# Request Models
# -------------------------------

class CrawlRequest(BaseModel):
    baseUrl: str


class AskRequest(BaseModel):
    question: str


# -------------------------------
# Crawl Endpoint
# -------------------------------

@app.post("/crawl")
def run_crawl(request: CrawlRequest):
    base_url = request.baseUrl

    crawler.visited = set()  # RESET visited

    crawl(base_url, base_url, "data/raw_pages")

    clean_all()
    embed_all()

    return {
        "status": "success",
        "message": "Website crawled and indexed successfully."
    }

# -------------------------------
# Ask Endpoint
# -------------------------------

@app.post("/ask")
def ask_question(request: AskRequest):
    return answer_question(request.question)