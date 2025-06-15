from flask import Flask, request, jsonify
from memory_utils import load_memory, save_memory
from gpt_client import generate_response
import os

app = Flask(__name__)

@app.route("/think/<agent>", methods=["POST"])
def think(agent):
    user_message = request.json.get("message", "")
    memory = load_memory(agent)
    response = generate_response(agent, memory, user_message)
    memory.append({"role": "assistant", "content": response})
    save_memory(agent, memory)
    return jsonify({"agent": agent, "response": response})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)