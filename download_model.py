import os
import sys
import gdown

def download_inswapper():
    """Download inswapper_128.onnx from Google Drive."""
    file_id = "1krOLgjW2tAPaqV-Bw4YALz0xT5zlb5HF"
    output_path = "models/inswapper_128.onnx"
    
    try:
        # Create models directory if it doesn't exist
        os.makedirs("models", exist_ok=True)
        
        # Skip if file already exists
        if os.path.isfile(output_path):
            print(f"✅ inswapper_128.onnx already exists")
            return True
            
        print(f"Downloading inswapper_128.onnx...")
        url = f"https://drive.google.com/uc?id={file_id}"
        
        # Download with progress bar
        gdown.download(url, output_path, quiet=False)
        
        if os.path.exists(output_path):
            print(f"✅ Downloaded inswapper_128.onnx")
            return True
        else:
            print(f"❌ Error: Failed to download inswapper_128.onnx")
            return False
            
    except Exception as e:
        print(f"❌ Error: Failed to download inswapper_128.onnx: {str(e)}")
        return False

def download_arcface():
    """Download arcface.onnx from Google Drive."""
    file_id = "1ps64Zyx_M-0909gXkQSodimLyUKRu_UL"
    output_path = "models/arcface.onnx"
    
    try:
        # Create models directory if it doesn't exist
        os.makedirs("models", exist_ok=True)
        
        # Skip if file already exists
        if os.path.isfile(output_path):
            print(f"✅ arcface.onnx already exists")
            return True
            
        print(f"Downloading arcface.onnx...")
        url = f"https://drive.google.com/uc?id={file_id}"
        
        # Download with progress bar
        gdown.download(url, output_path, quiet=False)
        
        if os.path.exists(output_path):
            print(f"✅ Downloaded arcface.onnx")
            return True
        else:
            print(f"❌ Error: Failed to download arcface.onnx")
            return False
            
    except Exception as e:
        print(f"❌ Error: Failed to download arcface.onnx: {str(e)}")
        return False

def download_model():
    """Download all required models if they don't exist."""
    success = True
    
    # Download inswapper model
    if not download_inswapper():
        success = False
    
    # Download arcface model
    if not download_arcface():
        success = False
    
    if not success:
        print("❌ Failed to download one or more models")
        sys.exit(1)
    
    print("✅ All models downloaded successfully")

if __name__ == "__main__":
    download_model() 