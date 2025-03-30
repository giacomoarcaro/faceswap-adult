import os
import requests

MODEL_URL = "https://huggingface.co/facefusion/facefusion-models/resolve/main/inswapper_128.onnx"
MODEL_PATH = "models/inswapper_128.onnx"

def download_model():
    os.makedirs("models", exist_ok=True)
    if not os.path.isfile(MODEL_PATH):
        print("Downloading inswapper_128.onnx...")
        response = requests.get(MODEL_URL, stream=True)
        with open(MODEL_PATH, "wb") as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        print("Model downloaded.")
    else:
        print("Model already exists.")

if __name__ == "__main__":
    download_model() 