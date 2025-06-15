import json
import os
from datetime import datetime

def load_memory(agent):
    path = f"memory/{agent}.json"
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

def save_memory(agent, message):
    path = f"memory/{agent}.json"
    memory = load_memory(agent)
    memory.append(message)
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(memory, f, ensure_ascii=False, indent=2)

def append_dialogue(speaker, content):
    dialogue_path = "dialogue/dialogue.json"
    if os.path.exists(dialogue_path):
        with open(dialogue_path, 'r', encoding='utf-8') as f:
            dialogue = json.load(f)
    else:
        dialogue = []

    dialogue.append({
        "speaker": speaker,
        "content": content,
        "ts": datetime.now().isoformat()
    })

    with open(dialogue_path, 'w', encoding='utf-8') as f:
        json.dump(dialogue, f, ensure_ascii=False, indent=2)

def load_last_dialogue(exclude_agent):
    dialogue_path = "dialogue/dialogue.json"
    if not os.path.exists(dialogue_path):
        return None
    with open(dialogue_path, 'r', encoding='utf-8') as f:
        dialogue = json.load(f)
    for entry in reversed(dialogue):
        if entry["speaker"] != exclude_agent:
            return entry
    return None
