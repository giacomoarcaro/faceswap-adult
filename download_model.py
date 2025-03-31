import os
import sys
import gdown

MODELS = {
    "inswapper_128.onnx": "1krOLgjW2tAPaqV-Bw4YALz0xT5zlb5HF",
    "arcface.onnx": "1Gne3Pd3UzQZCCcGm7DLaP97CEFrhO6wE"
}

def download_file(file_id: str, output_path: str) -> bool:
    """Download a file from Google Drive using gdown."""
    try:
        url = f"https://drive.google.com/uc?id={file_id}"
        print(f"Downloading {os.path.basename(output_path)}...")
        
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
    for filename, file_id in MODELS.items():
        model_path = os.path.join("models", filename)
        
        # Skip if file already exists
        if os.path.isfile(model_path):
            print(f"✅ {filename} already exists")
            continue
            
        # Download the file
        if not download_file(file_id, model_path):
            success = False
            break
    
    if not success:
        print("❌ Failed to download one or more models")
        sys.exit(1)
    
    print("✅ All models downloaded successfully")

if __name__ == "__main__":
    download_models() 