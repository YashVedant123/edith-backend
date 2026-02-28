import json
import os

LOG_FILE = "storage/conversation_log.json"

def log_message(user_id, message, response):
    if not os.path.exists(LOG_FILE):
        data = {}
    else:
        with open(LOG_FILE, "r") as f:
            data = json.load(f)

    data.setdefault(user_id, [])
    data[user_id].append({
        "message": message,
        "response": response
    })

    with open(LOG_FILE, "w") as f:
        json.dump(data, f, indent=2)