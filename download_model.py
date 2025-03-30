import os
import sys
import requests
from tqdm import tqdm

MODEL_URL = "https://huggingface.co/facefusion/facefusion-models/resolve/main/inswapper_128.onnx"
MODEL_PATH = "models/inswapper_128.onnx"

def download_model():
    """Download the model file if it doesn't exist."""
    try:
        # Create models directory if it doesn't exist
        os.makedirs("models", exist_ok=True)
        
        # Check if model already exists
        if os.path.isfile(MODEL_PATH):
            print(f"Model already exists at {MODEL_PATH}")
            return MODEL_PATH
            
        print(f"Downloading model from {MODEL_URL}...")
        
        # Download with progress bar
        response = requests.get(MODEL_URL, stream=True)
        response.raise_for_status()  # Raise an exception for bad status codes
        
        total_size = int(response.headers.get('content-length', 0))
        block_size = 8192
        
        with open(MODEL_PATH, 'wb') as f, tqdm(
            desc="Downloading",
            total=total_size,
            unit='iB',
            unit_scale=True,
            unit_divisor=1024,
        ) as pbar:
            for chunk in response.iter_content(chunk_size=block_size):
                size = f.write(chunk)
                pbar.update(size)
                
        print(f"Model downloaded successfully to {MODEL_PATH}")
        return MODEL_PATH
        
    except requests.exceptions.RequestException as e:
        print(f"Error downloading model: {str(e)}")
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    download_model() 