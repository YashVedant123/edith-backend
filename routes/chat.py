from core.gemini_client import generate_response
from core.context_builder import build_context
from core.conversation_manager import log_message
from core.memory_manager import get_user_memory

def handle_chat(data):
    user_id = data.get("user_id")
    message = data.get("message")

    if message.lower().startswith("open "):
        return {"response": "COMMAND:OPEN_BROWSER"}
    
    memory = get_user_memory(user_id)
    memory_text = str(memory)

    response = generate_response(message, memory_text)
    prompt = build_context(user_id, message)
    response = generate_response(prompt)

    log_message(user_id, message, response)

    return {"response": response}
    