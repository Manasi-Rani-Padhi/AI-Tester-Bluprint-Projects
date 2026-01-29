# Findings & Research

## Exploratory Research
- **Local LLM Infrastructure**: Ollama is installed and running.
- **Available Models**:
    - `qwen2:0.5b` (Small, fast, low resource)
    - `llama3.2:3b` (Medium, better reasoning)
- **Environment**: Linux environment with `python` (assumed) and `npm` available.
- **Ollama API Integration**:
    - Official Python library: `ollama-python`.
    - Endpoints: `/api/generate` (one-shot) and `/api/chat` (conversational).
    - Features: Supports streaming, tool calling, and custom `Modelfile` for system prompts.
    - JSON Mode: Ollama supports `format: "json"` in API calls to ensure structured output.
- **Resource Constraints**:
    - `llama3.2:3b` requires ~2.3 GiB RAM (Currently only 1.4 GiB available).
    - `qwen2:0.5b` is responsive and fits within memory limits.

## Constraints
- Must use Ollama for local LLM execution.
- Must follow BLAST protocol.

## Discoveries
- (To be populated during discovery phase)
