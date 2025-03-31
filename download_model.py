import os
import sys
import requests
from tqdm import tqdm

MODELS = {
    "inswapper_128.onnx": "https://github.com/facefusion/facefusion-assets/releases/download/models/inswapper_128.onnx",
    "arcface.onnx": "https://github.com/facefusion/facefusion-assets/releases/download/models/arcface.onnx"
}

def download_file(url: str, filename: str) -> bool:
    """Download a file with progress bar."""
    try:
        print(f"Downloading {filename}...")
        response = requests.get(url, stream=True)
        response.raise_for_status()
        
        total_size = int(response.headers.get('content-length', 0))
        block_size = 8192
        
        with open(filename, 'wb') as f, tqdm(
            desc=filename,
            total=total_size,
            unit='iB',
            unit_scale=True,
            unit_divisor=1024,
        ) as pbar:
            for chunk in response.iter_content(chunk_size=block_size):
                size = f.write(chunk)
                pbar.update(size)
        
        print(f"✅ Downloaded {filename}")
        return True
        
    except Exception as e:
        print(f"❌ Error: Failed to download {filename}: {str(e)}")
        return False

def download_models():
    """Download all required models if they don't exist."""
    # Create models directory if it doesn't exist
    os.makedirs("models", exist_ok=True)
    
    success = True
    for filename, url in MODELS.items():
        model_path = os.path.join("models", filename)
        
        # Skip if file already exists
        if os.path.isfile(model_path):
            print(f"✅ {filename} already exists")
            continue
            
        # Download the file
        if not download_file(url, model_path):
            success = False
            break
    
    if not success:
        print("❌ Failed to download one or more models")
        sys.exit(1)
    
    print("✅ All models downloaded successfully")

if __name__ == "__main__":
    download_models() 