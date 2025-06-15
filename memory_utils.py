import json
import os

def memory_path(agent):
    return f"memory/{agent}.json"

def load_memory(agent):
    path = memory_path(agent)
    if not os.path.exists(path):
        return []
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def save_memory(agent, memory):
    path = memory_path(agent)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(memory, f, ensure_ascii=False, indent=2)