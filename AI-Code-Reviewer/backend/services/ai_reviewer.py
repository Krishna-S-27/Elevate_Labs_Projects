import os
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

def run_ai_reviewer(code: str, language: str = "java"):
    if not OPENROUTER_API_KEY:
        return "Error: OPENROUTER_API_KEY not set in .env"

    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }

    # Use your chosen model: gpt-oss-20b (free)
    data = {
        "model": "openai/gpt-oss-20b",
        "messages": [
            {"role": "system", "content": "You are an expert software code reviewer."},
            {"role": "user", "content": f"Please review this {language} code:\n\n{code}"}
        ]
    }

    try:
        response = requests.post(url, headers=headers, json=data)
        if response.status_code == 200:
            return response.json()["choices"][0]["message"]["content"]
        else:
            return f"AI Error: {response.text}"
    except Exception as e:
        return f"AI Review failed: {str(e)}"
