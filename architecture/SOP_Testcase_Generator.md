# SOP: Testcase Generator Logic

## Goal
Transform user requirements into structured test cases using a predefined template.

## Inputs
- `user_input`: The feature description.
- `template`: (To be provided by user) The system prompt or instruction set.

## Tool Logic (`tools/tc_engine.py`)
1. Load the "Proper Template" from the code configuration.
2. Inject `user_input` into the template.
3. Call `SOP_Ollama_Proxy` with `json_mode=True`.
4. Validate the returning JSON against the schema in `gemini.md`.
5. If validation fails, attempt one "self-healing" retry with an error-correction prompt.
6. Return the finalized JSON payload.

## Edge Cases
- Empty input: Prompt user for details.
- Hallucinated JSON: Attempt to extract JSON using regex if parsing fails.
