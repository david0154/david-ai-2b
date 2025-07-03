import os
import requests
import zipfile

# Download links for pretrained open-source models
MODEL_URLS = {
    "chat": "https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.1/resolve/main/model.safetensors",
    "code": "https://huggingface.co/bigcode/starcoderbase-1b/resolve/main/model.bin",
    "image_gen": "https://huggingface.co/runwayml/stable-diffusion-v1-5/resolve/main/sd-v1-5-inference.zip",
    "deblur": "https://github.com/xinntao/Real-ESRGAN/releases/download/v0.2.5/RealESRGAN_x4plus.pth",
    "edge": "https://github.com/xuebinqin/U-2-Net/releases/download/v1.0/u2net.pth",
    "vosk": "https://alphacephei.com/vosk/models/vosk-model-small-hi-0.22.zip",
    "indictrans": "https://indicnlp-models.s3.amazonaws.com/indictrans2/ai4bharat/indictrans2-en-indic.zip"
}

def download_file(url, dest_path):
    print(f"⬇️ Downloading: {url}")
    response = requests.get(url, stream=True)
    total = int(response.headers.get('content-length', 0))
    with open(dest_path, 'wb') as file, \
         open(dest_path + ".part", 'wb') as progress_file:
        for chunk in response.iter_content(chunk_size=1024):
            if chunk:
                file.write(chunk)
    print(f"✅ Downloaded: {dest_path}")

def extract_zip(file_path, extract_to):
    print(f"📦 Extracting: {file_path}")
    with zipfile.ZipFile(file_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)
    os.remove(file_path)

def ensure_dir(path):
    os.makedirs(path, exist_ok=True)

def bootstrap():
    if os.path.exists("models/.downloaded"):
        print("✅ Models already downloaded. Skipping.")
        return

    print("🚀 Downloading all AI models (one-time setup)...")
    ensure_dir("models")

    for name, url in MODEL_URLS.items():
        dest_folder = os.path.join("models", name)
        ensure_dir(dest_folder)

        filename = url.split("/")[-1]
        dest_file = os.path.join(dest_folder, filename)

        if not os.path.exists(dest_file):
            download_file(url, dest_file)
            if dest_file.endswith(".zip"):
                extract_zip(dest_file, dest_folder)

    open("models/.downloaded", "w").write("done")
    print("✅ All AI models downloaded successfully.")
