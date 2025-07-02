import os
from flask import Flask, request, jsonify
import threading

# Import AI modules (we'll add full logic later)
from app.ai.chat_ai import chat_response
from app.ai.code_ai import generate_code
from app.ai.image_gen import generate_image
from app.ai.deblur_ai import deblur_image
from app.voice.voice_input import start_voice_listener
from app.ui.frontend import start_gui

app = Flask(__name__)

# ------------------- API ROUTES ---------------------

@app.route("/api/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message")
    response = chat_response(user_input)
    return jsonify({"response": response})

@app.route("/api/code", methods=["POST"])
def code():
    code_input = request.json.get("prompt")
    result = generate_code(code_input)
    return jsonify({"result": result})

@app.route("/api/image", methods=["POST"])
def image_gen():
    prompt = request.json.get("prompt")
    path = generate_image(prompt)
    return jsonify({"image_path": path})

@app.route("/api/deblur", methods=["POST"])
def deblur():
    image_path = request.json.get("image_path")
    result = deblur_image(image_path)
    return jsonify({"output_path": result})

# ----------------- APP LAUNCHER ---------------------

def launch_server_or_gui():
    # Start Flask server in a separate thread
    flask_thread = threading.Thread(target=lambda: app.run(port=7860))
    flask_thread.start()

    # Start voice listener in another thread
    voice_thread = threading.Thread(target=start_voice_listener)
    voice_thread.start()

    # Start GUI (main thread)
    start_gui()
