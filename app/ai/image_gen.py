import torch
from diffusers import StableDiffusionPipeline
import os
from datetime import datetime

model = None

def load_model():
    global model
    if model is None:
        print("🖼️ Loading Stable Diffusion v1.5...")
        model_path = "models/image_gen"
        model = StableDiffusionPipeline.from_pretrained(
            model_path,
            torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32
        )
        if torch.cuda.is_available():
            model = model.to("cuda")
    return model

def generate_image(prompt: str) -> str:
    model = load_model()
    image = model(prompt).images[0]
    
    out_dir = "output/images"
    os.makedirs(out_dir, exist_ok=True)
    filename = f"{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
    image_path = os.path.join(out_dir, filename)
    image.save(image_path)
    
    print(f"🖼️ Image saved: {image_path}")
    return image_path
