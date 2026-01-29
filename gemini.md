# Project Constitution (Gemini)

## 1. Identity & Goals
Build a reliable, local-first test case generator.

## 2. Data Schemas

### Input Payload (User -> Generator)
```json
{
  "user_input": "String (Feature description or user requirement)"
}
```

### Output Payload (LLM -> UI)
```json
{
  "summary": "String (Short summary of the test suite)",
  "test_cases": [
    {
      "id": "TC-00x",
      "title": "String",
      "preconditions": "String",
      "steps": ["Step 1", "Step 2", "..."],
      "expected_result": "String",
      "priority": "High | Medium | Low"
    }
  ]
}
```

## 3. Behavioral Rules
- Use only local Ollama for generations.
- Output must be valid Markdown or JSON as requested.
- Ensure deterministic output structure.

## 4. Architectural Invariants
- Separation of LLM client logic and prompt engineering logic.
- Self-healing retries for JSON parsing if needed.
