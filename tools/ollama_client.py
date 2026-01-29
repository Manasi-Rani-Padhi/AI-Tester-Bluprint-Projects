import requests
import json

class OllamaClient:
    def __init__(self, base_url="http://localhost:11434", model="qwen2:0.5b"):
        self.base_url = base_url
        self.model = model

    def generate(self, prompt, json_mode=False):
        url = f"{self.base_url}/api/generate"
        payload = {
            "model": self.model,
            "prompt": prompt,
            "stream": False
        }
        if json_mode:
            payload["format"] = "json"

        try:
            response = requests.post(url, json=payload, timeout=60)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            return {"error": str(e)}

    def check_memory_and_switch(self):
        # Logic to check if llama3.2 can be used, else fallback
        # (Based on our Link phase findings, we stay with qwen2 for now)
        pass
