import google.generativeai as genai

GEMINI_API_KEY = "AIzaSyBgqmmkNZB2-caq5qCJVJMU0_ymX_ilD4w"
genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("models/gemini-2.5-flash")

def generate_response(prompt: str):
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        print("Gemini API error:", e)
        return "Sorry, I could not generate a response."
    
SYSTEM_PROMPT = """
You are EDITH, a highly intelligent personal AI assistant.
You respond naturally, intelligently, and concisely.
You remember the user's preferences and adapt to them.
You understand intent beyond literal words.
You can distinguish between casual conversation and commands.
"""

def generate_response(user_prompt: str, memory_context: str = ""):
    try:
        full_prompt = f"""
{SYSTEM_PROMPT}

User Memory:
{memory_context}

User Message:
{user_prompt}
"""
        response = model.generate_content(full_prompt)
        return response.text
    except Exception as e:
        print("Gemini API error:", e)
        return "I'm having trouble processing that."