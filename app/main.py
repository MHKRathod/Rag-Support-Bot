from fastapi import FastAPI
from app.rag import answer_question

app = FastAPI()

@app.get("/ask")
def ask(q: str):
    return {"answer": answer_question(q)}
