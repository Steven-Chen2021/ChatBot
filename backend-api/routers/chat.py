from fastapi import APIRouter
from pydantic import BaseModel

from ..gemini_connector import query_gemini
from ..prompt_engine import build_prompt


router = APIRouter(prefix="/chat", tags=["chat"])


class ChatRequest(BaseModel):
    message: str


class ChatResponse(BaseModel):
    response: str


@router.post("/", response_model=ChatResponse)
def chat(request: ChatRequest):
    """Proxy user message to the Gemini API."""
    prompt = build_prompt(request.message)
    response_text = query_gemini(prompt)
    return ChatResponse(response=response_text)
