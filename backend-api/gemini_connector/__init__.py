"""Simple Gemini API connector stub."""

import requests

GEMINI_ENDPOINT = "https://gemini-api.example.com/query"
API_KEY = "YOUR_API_KEY"


def query_gemini(prompt: str) -> str:
    """Send the prompt to the Gemini API and return the response text."""
    try:
        response = requests.post(
            GEMINI_ENDPOINT,
            json={"prompt": prompt},
            headers={"Authorization": f"Bearer {API_KEY}"},
            timeout=10,
        )
        response.raise_for_status()
        data = response.json()
        return data.get("response", "")
    except requests.RequestException:
        # In this demo environment we simply echo the prompt
        return f"Gemini response for: {prompt}"
