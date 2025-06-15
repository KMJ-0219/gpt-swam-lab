import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_response(agent, memory, user_message=""):
    system_prompt = f"You are {agent.upper()}, an AI agent with unique personality. Respond accordingly."
    messages = [{"role": "system", "content": system_prompt}] + memory
    if user_message:
        messages.append({"role": "user", "content": user_message})
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=0.7
    )
    return completion.choices[0].message["content"]