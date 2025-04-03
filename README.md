# Local LLM API

This is a FastAPI application that accepts HTTP requests with questions and returns responses using a local LLM model.

## Setup

1. Install the required dependencies:
```bash
pip install -r requirements.txt
```

2. Download a GGUF format LLM model (e.g., from Hugging Face) and update the `MODEL_PATH` in `app.py` with the path to your model file.

## Running the Application

Start the server with:
```bash
python app.py
```

The server will run on `http://localhost:8000`

## API Endpoints

- `GET /`: Health check endpoint
- `POST /ask`: Send a question to the LLM

### Example Usage

Using curl:
```bash
curl -X POST "http://localhost:8000/ask" \
     -H "Content-Type: application/json" \
     -d '{"text": "What is the capital of France?"}'
```

Using Python requests:
```python
import requests

response = requests.post(
    "http://localhost:8000/ask",
    json={"text": "What is the capital of France?"}
)
print(response.json())
```

## API Documentation

Once the server is running, you can access the interactive API documentation at:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc` 
