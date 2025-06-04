from fastapi import FastAPI

from .routers import chat, admin, status

app = FastAPI(title="ChatBot Backend")

app.include_router(chat.router)
app.include_router(admin.router)
app.include_router(status.router)


@app.get("/")
def root():
    """Basic health check endpoint."""
    return {"message": "AI Chatbot Backend Running"}
