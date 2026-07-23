import os
import requests
from dotenv import load_dotenv

load_dotenv()


class QwenService:

    def __init__(self):
        self.model_name = os.getenv("OLLAMA_MODEL", "qwen2.5:1.5b")
        self.base_url = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")

    def generate(self, prompt: str) -> str:
        response = requests.post(
            f"{self.base_url}/api/generate",
            json={
                "model": self.model_name,
                "prompt": prompt,
                "stream": False
            },
            timeout=300
        )

        response.raise_for_status()

        return response.json()["response"]