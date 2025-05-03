# filepath: c:\Project\ChatBot\backend-api\gemini_connector\__init__.py
import requests

# Connects and sends prompt to Gemini API
def query_gemini(prompt: str):
    response = requests.post(
        "https://gemini-api.example.com/query",
        json={"prompt": prompt},
        headers={"Authorization": "Bearer YOUR_API_KEY"}
    )
    return response.json()