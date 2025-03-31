import os
import sys
import requests
import gdown
from tqdm import tqdm

MODELS = {
    "inswapper_128.onnx": {
        "type": "gdrive",
        "id": "1krOLgjW2tAPaqV-Bw4YALz0xT5zlb5HF"
    },
    "arcface.onnx": {
        "type": "github",
        "url": "https://github.com/deepinsight/insightface/releases/download/v0.7/arcface.onnx"
    }
}

def download_from_github(url: str, output_path: str) -> bool:
    """Download a file from GitHub using requests."""
    try:
        print(f"Downloading {os.path.basename(output_path)}...")
        response = requests.get(url, stream=True)
        response.raise_for_status()
        
        total_size = int(response.headers.get('content-length', 0))
        block_size = 8192
        
        with open(output_path, 'wb') as f, tqdm(
            desc=os.path.basename(output_path),
            total=total_size,
            unit='iB',
            unit_scale=True,
            unit_divisor=1024,
        ) as pbar:
            for chunk in response.iter_content(chunk_size=block_size):
                size = f.write(chunk)
                pbar.update(size)
        
        print(f"✅ Downloaded {os.path.basename(output_path)}")
        return True
        
    except Exception as e:
        print(f"❌ Error: Failed to download {os.path.basename(output_path)}: {str(e)}")
        return False

def download_from_gdrive(file_id: str, output_path: str) -> bool:
    """Download a file from Google Drive using gdown."""
    try:
        print(f"Downloading {os.path.basename(output_path)}...")
        url = f"https://drive.google.com/uc?id={file_id}"
        
        # Download with progress bar
        gdown.download(url, output_path, quiet=False)
        
        if os.path.exists(output_path):
            print(f"✅ Downloaded {os.path.basename(output_path)}")
            return True
        else:
            print(f"❌ Error: Failed to download {os.path.basename(output_path)}")
            return False
            
    except Exception as e:
        print(f"❌ Error: Failed to download {os.path.basename(output_path)}: {str(e)}")
        return False

def download_models():
    """Download all required models if they don't exist."""
    # Create models directory if it doesn't exist
    os.makedirs("models", exist_ok=True)
    
    success = True
    for filename, model_info in MODELS.items():
        model_path = os.path.join("models", filename)
        
        # Skip if file already exists
        if os.path.isfile(model_path):
            print(f"✅ {filename} already exists")
            continue
            
        # Download based on model type
        if model_info["type"] == "gdrive":
            if not download_from_gdrive(model_info["id"], model_path):
                success = False
                break
        elif model_info["type"] == "github":
            if not download_from_github(model_info["url"], model_path):
                success = False
                break
    
    if not success:
        print("❌ Failed to download one or more models")
        sys.exit(1)
    
    print("✅ All models downloaded successfully")

if __name__ == "__main__":
    download_models() 