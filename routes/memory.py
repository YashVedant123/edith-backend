from core.memory_manager import remember, recall

def handle_memory(data):
    action = data.get("action")
    user_id = data.get("user_id")
    key = data.get("key")
    value = data.get("value")

    if action == "remember":
        remember(user_id, key, value)
        return {"status": "saved"}

    if action == "recall":
        result = recall(user_id, key)
        return {"value": result}

    return {"error": "Invalid memory action"}