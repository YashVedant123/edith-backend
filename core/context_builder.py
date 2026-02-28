from core.memory_manager import load_memory

def build_context(user_id, message):
    memory = load_memory().get(user_id, {})
    memory_text = "\n".join([f"{k}: {v}" for k, v in memory.items()])

    return f"""
You are EDITH AI.

User Memory:
{memory_text}

User says:
{message}
"""