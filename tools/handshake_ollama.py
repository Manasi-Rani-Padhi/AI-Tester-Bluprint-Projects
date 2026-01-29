import requests
import json
import sys

def verify_ollama(model_name):
    url = "http://localhost:11434/api/generate"
    payload = {
        "model": model_name,
        "prompt": "hi",
        "stream": False
    }
    
    print(f"Testing model: {model_name}...")
    try:
        response = requests.post(url, json=payload, timeout=60)
        if response.status_code == 200:
            print(f"✅ Model {model_name} is responsive.")
            return True
        else:
            print(f"❌ Model {model_name} returned status {response.status_code}: {response.text}")
            return False
    except Exception as e:
        print(f"Error connecting to Ollama for {model_name}: {e}")
        return False

if __name__ == "__main__":
    qwen_ok = verify_ollama("qwen2:0.5b")
    llama_ok = verify_ollama("llama3.2:3b")
    
    if qwen_ok or llama_ok:
        print("✅ PHASE 2: AT LEAST ONE MODEL IS RESPONSIVE")
        sys.exit(0)
    else:
        print("❌ PHASE 2: LINK FAILED")
        sys.exit(1)
