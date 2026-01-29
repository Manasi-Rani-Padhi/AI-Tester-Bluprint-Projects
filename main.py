from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from tools.tc_engine import TCEngine
import uvicorn
import os

app = FastAPI(title="Local LLM Testcase Generator")

# Enable CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

engine = TCEngine()

class UserInput(BaseModel):
    user_input: str

@app.post("/generate")
async def generate_testcases(data: UserInput):
    if not data.user_input:
        raise HTTPException(status_code=400, detail="Input cannot be empty")
    
    result = engine.generate_test_cases(data.user_input)
    if "error" in result:
        raise HTTPException(status_code=500, detail=result["error"])
    
    return result

# Serve static files (Frontend)
if os.path.exists("static"):
    app.mount("/", StaticFiles(directory="static", html=True), name="static")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
