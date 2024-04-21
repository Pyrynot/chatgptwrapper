from fastapi import FastAPI, HTTPException, Security, Depends
from fastapi.security.api_key import APIKeyHeader
from models import ChatRequest
from fastapi.middleware.cors import CORSMiddleware
from openai import AsyncOpenAI
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_API_URL = os.getenv("OPENAI_API_URL")

# Initialize app. not sure if CORS is needed but added it anyway. might need to tweak settings
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["POST"],
    allow_headers=["X-API-KEY"]
)

api_key_header = APIKeyHeader(name="X-API-KEY", auto_error=False)

def api_key_auth(api_key: str = Security(api_key_header)):
    if api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Missing or invalid API key")

client = AsyncOpenAI(
    api_key=OPENAI_API_KEY
)

@app.post("/chat/")
async def create_chat_completion(request: ChatRequest, api_key: str = Depends(api_key_auth)):
    """
    API endpoint that takes the same arguments as the real chatGPT API (except stream)
    and returns the JSON object from chatGPT directly.

    Params:
    request: Validated against the ChatRequest model.
    api_key: X-API-KEY header with the key inside the POST-request

    Returns:
    response in json format directly from ChatGPT API.
    """
    # Dump the model into a dict and exclude non-specified values
    request_dict = request.model_dump(exclude_none=True)
    try:
        response = await client.chat.completions.create(**request_dict)
    except Exception as e:
        print(f"Error while contacting OpenAI API: {str(e)}")
        raise HTTPException(status_code=500, detail="Error contacting OpenAI API")
    return response