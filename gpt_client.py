from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_response(agent_name, memory, user_message):
    messages = [
        {"role": "system", "content": f"너는 {agent_name} 인격이야. 이건 너의 기억이다: {memory}"},
        {"role": "user", "content": user_message}
    ]

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=0.7
    )

    return response.choices[0].message.content
