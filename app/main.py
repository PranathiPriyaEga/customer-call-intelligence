from fastapi import FastAPI
from pydantic import BaseModel

from app.llm_service import analyze_call


app = FastAPI(
    title="Enterprise IT Support Intelligence API",
    description="AI-powered enterprise IT support analysis using NLP, RAG, and Gemma 3.",
    version="1.0.0"
)


class SupportRequest(BaseModel):
    conversation: str


@app.get("/")
def root():
    return {
        "message": "Enterprise IT Support Intelligence API",
        "status": "running"
    }


@app.post("/analyze")
def analyze_support_request(request: SupportRequest):

    result = analyze_call(
        request.conversation
    )

    return result
