import os
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
API_SECRET = os.getenv("API_SECRET", "edith-secret")
PORT = int(os.getenv("PORT", 8000))
