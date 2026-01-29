# Task Plan - Local LLM Testcase Generator

## Project Overview
Create a local LLM-powered test case generator using Ollama to automate the creation of software test cases based on user-provided prompts or feature descriptions.

## Phases
### Phase 1: Exploration & Blueprinting (Complete)
- [x] Define Discovery Questions
- [x] Answer Discovery Questions
- [x] Define Data Schema in `gemini.md`
- [x] Finalize Blueprint

### Phase 2: Linking & Setup
- [ ] Verify Ollama connection (`llama3.2:3b`)
- [ ] Initialize Python/Node.js backend (FastAPI/Express)
- [ ] Setup frontend (HTML/CSS/JS)

### Phase 3: Architecture (The 3-Layer Build) (Complete)
- [x] Implement Layer 1: Technical SOPs in `architecture/`.
- [x] Implement Layer 3: Deterministic Tools in `tools/`.
- [x] Implement Layer 2: Navigation logic in `main.py`.
- [x] Build `ollama_proxy`: Backend to handle Ollama API calls.
- [x] Build `prompt_engine`: Stores the "Proper Template".
- [x] Build `chat_ui`: Premium glassmorphic chat interface.

### Phase 4: Stylizing & Refining (Complete)
- [x] Glassmorphic UI Design refinement.
- [x] Priority-based color coding for test cases.
- [x] Markdown rendering inside chat bubbles.
- [x] "Copy to Markdown" action for professional delivery.

### Phase 5: Trigger & Delivery
- [ ] Launch local server.
- [ ] Final end-to-end traversal.

## Checklist
- [ ] Protocol 0: Initialization complete
- [ ] Schema defined
- [ ] Plan approved
