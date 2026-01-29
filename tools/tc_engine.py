from tools.ollama_client import OllamaClient
from tools.config import TEST_CASE_TEMPLATE
import json

class TCEngine:
    def __init__(self):
        self.client = OllamaClient()

    def generate_test_cases(self, user_input):
        prompt = TEST_CASE_TEMPLATE.format(user_input=user_input)
        response = self.client.generate(prompt, json_mode=True)
        
        if "error" in response:
            return response
        
        try:
            # The 'response' field in Ollama's output contains the JSON string
            content = response.get("response", "")
            return json.loads(content)
        except json.JSONDecodeError:
            return {"error": "Failed to parse LLM response into JSON", "raw": response.get("response")}

if __name__ == "__main__":
    engine = TCEngine()
    test_input = "Login page with email and password"
    print(json.dumps(engine.generate_test_cases(test_input), indent=2))
