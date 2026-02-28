import json
import os


MEMORY_FILE = "storage/edith_memory.json"

def load_memory():
    if not os.path.exists(MEMORY_FILE):
        return {}
    with open(MEMORY_FILE, "r") as f:
        return json.load(f)

def save_memory(data):
    with open(MEMORY_FILE, "w") as f:
        json.dump(data, f, indent=2)

def remember(user_id, key, value):
    memory = load_memory()
    memory.setdefault(user_id, {})
    memory[user_id][key] = value
    save_memory(memory)

def recall(user_id, key):
    memory = load_memory()
    return memory.get(user_id, {}).get(key)

# Simple in-memory storage
memory_store = {}

def get_user_memory(user_id):
    return memory_store.get(user_id, [])

def add_to_memory(user_id, message):
    if user_id not in memory_store:
        memory_store[user_id] = []

    memory_store[user_id].append(message)