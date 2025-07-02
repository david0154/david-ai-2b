import os
from llama_cpp import Llama

MODEL_PATH = "models/chat/mistral-7b-instruct.ggml.q4_0.bin"

llm = None

def load_model():
    global llm
    if llm is None:
        print("🔁 Loading Mistral-7B model...")
        llm = Llama(
            model_path=MODEL_PATH,
            n_ctx=2048,
            n_threads=6,
            n_gpu_layers=35  # Use 0 for CPU-only, or adjust for your GPU
        )
    return llm

def chat_response(prompt: str) -> str:
    model = load_model()
    system_prompt = "You are David AI 2B, a helpful offline assistant developed by Nexuzy Tech and David."
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": prompt}
    ]
    response = model.create_chat_completion(
        messages=messages,
        temperature=0.7,
        top_p=0.9,
        max_tokens=512
    )
    return response['choices'][0]['message']['content']
