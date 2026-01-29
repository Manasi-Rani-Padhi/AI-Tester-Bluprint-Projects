# SOP: Ollama Proxy Logic

## Goal
Provide a deterministic interface to the local Ollama API.

## Inputs
- `model`: Model name (default: qwen2:0.5b)
- `prompt`: The formatted string to send.
- `json_mode`: Boolean to enforce JSON output.

## Tool Logic (`tools/ollama_client.py`)
1. Receive request from the Navigation layer.
2. Send POST request to `http://localhost:11434/api/generate`.
3. If `json_mode` is true, ensure `format="json"` is passed to Ollama.
4. Handle 500 errors (Memory constraints) and timeout.
5. Return the raw response or parsed JSON.

## Edge Cases
- Ollama service down: Return clear error message.
- Memory overflow: Return error suggesting model swap.
- Timeout: Retry once then fail.
