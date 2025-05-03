from fastapi import FastAPI
from routers import chat, admin, status

app = FastAPI()

app.include_router(chat.router)
app.include_router(admin.router)
app.include_router(status.router)

@app.get('/')
def root():
    return {"message": "AI Chatbot Backend Running"}