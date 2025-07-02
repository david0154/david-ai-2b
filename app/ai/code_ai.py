import os
from transformers import AutoTokenizer, AutoModelForCausalLM

model = None
tokenizer = None

def load_model():
    global model, tokenizer
    if model is None or tokenizer is None:
        print("🔁 Loading StarCoder-1B for code generation...")
        model_path = "models/code"
        tokenizer = AutoTokenizer.from_pretrained(model_path)
        model = AutoModelForCausalLM.from_pretrained(model_path)
    return model, tokenizer

def generate_code(prompt: str) -> str:
    model, tokenizer = load_model()
    inputs = tokenizer(prompt, return_tensors="pt", truncation=True)
    output = model.generate(**inputs, max_new_tokens=200)
    result = tokenizer.decode(output[0], skip_special_tokens=True)
    return result.strip()
