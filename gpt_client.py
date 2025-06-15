import openai
import os
import json

def chat_with_gpt(agent_name, prompt, memory, last_opponent_message=None):
    system_prompt = prompt.strip()

    messages = [{"role": "system", "content": system_prompt}]

    if last_opponent_message:
        messages.append({
            "role": "assistant",
            "content": f"{last_opponent_message['speaker']}: {last_opponent_message['content']}"
        })
        messages.append({
            "role": "user",
            "content": "너의 생각은 어때?"
        })

    for mem in memory:
        messages.append({"role": "assistant", "content": mem})

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=messages,
        temperature=0.7,
        api_key=os.getenv("OPENAI_API_KEY")
    )
    return response.choices[0].message["content"].strip()
