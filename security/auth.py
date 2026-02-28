from config import API_SECRET

def verify_api_key(headers):
    return headers.get("X-API-KEY") == API_SECRET