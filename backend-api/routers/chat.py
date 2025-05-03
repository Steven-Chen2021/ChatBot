from fastapi import APIRouter
from gemini_connector import query_gemini

router = APIRouter(prefix='/chat')

@router.post('/')
def chat(prompt: str):
    response = query_gemini(prompt)
    return {"response": response}