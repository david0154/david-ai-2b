from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

MODEL_PATH = "models/chat"
model = None
tokenizer = None

def load_model():
    global model, tokenizer
    if model is None or tokenizer is None:
        print("🔁 Loading Mistral-7B for chat...")
        tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)
        model = AutoModelForCausalLM.from_pretrained(
            MODEL_PATH,
            torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32,
            low_cpu_mem_usage=True
        )
        if torch.cuda.is_available():
            model = model.cuda()
    return model, tokenizer

def chat_response(prompt: str) -> str:
    model, tokenizer = load_model()
    
    # Format the prompt
    full_prompt = f"<s>[INST] {prompt} [/INST]"
    
    # Generate response
    inputs = tokenizer(full_prompt, return_tensors="pt")
    if torch.cuda.is_available():
        inputs = {k: v.cuda() for k, v in inputs.items()}
    
    # Generate with standard parameters
    outputs = model.generate(
        **inputs,
        max_new_tokens=512,
        temperature=0.7,
        top_p=0.95,
        repetition_penalty=1.1
    )
    
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    # Clean up the response to only get the model's reply
    response = response.split("[/INST]")[-1].strip()
    
    return response
