from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from llama_cpp import Llama
import os

app = FastAPI(title="Local LLM API")

# Initialize the LLM model
# Note: You'll need to download a model file and specify its path
MODEL_PATH = "path/to/your/model.gguf"  # Update this with your model path
try:
    llm = Llama(model_path=MODEL_PATH)
except Exception as e:
    print(f"Error loading model: {e}")
    llm = None

class Question(BaseModel):
    text: str

@app.get("/")
async def root():
    return {"message": "Local LLM API is running"}

@app.post("/ask")
async def ask_question(question: Question):
    if llm is None:
        raise HTTPException(status_code=500, detail="LLM model not loaded")
    
    try:
        # Generate response using the local LLM
        response = llm(
            question.text,
            max_tokens=256,
            stop=["Q:", "\n"],
            echo=False
        )
        
        return {"response": response['choices'][0]['text'].strip()}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000) 