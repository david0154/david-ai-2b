import os
import queue
import sounddevice as sd
import vosk
import json
from langdetect import detect

q = queue.Queue()

MODEL_DIR = "models/vosk"  # This should contain subfolders like `hi` or `bn`
LANG_MODELS = {
    "en": "vosk-model-small-en-us-0.15",
    "hi": "vosk-model-small-hi-0.22",
    "bn": "vosk-model-small-bn-0.22"
}

def get_language_model(lang_code):
    folder = LANG_MODELS.get(lang_code, LANG_MODELS["en"])
    model_path = os.path.join(MODEL_DIR, folder)
    if not os.path.exists(model_path):
        raise FileNotFoundError(f"Vosk model not found: {model_path}")
    return vosk.Model(model_path)

def callback(indata, frames, time, status):
    if status:
        print(status)
    q.put(bytes(indata))

def start_voice_listener():
    try:
        print("🎤 Starting offline voice listener (Press Ctrl+C to stop)...")
        lang = "hi"  # You can make this dynamic later
        model = get_language_model(lang)
        with sd.RawInputStream(samplerate=16000, blocksize=8000, dtype='int16',
                               channels=1, callback=callback):
            rec = vosk.KaldiRecognizer(model, 16000)
            while True:
                data = q.get()
                if rec.AcceptWaveform(data):
                    result = json.loads(rec.Result())
                    text = result.get("text", "")
                    if text:
                        print(f"🗣️ You said: {text}")
    except KeyboardInterrupt:
        print("🛑 Voice listener stopped.")
