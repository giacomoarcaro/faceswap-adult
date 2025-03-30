import os
import shutil
import tempfile
from pathlib import Path
from typing import Optional
from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import cv2
import numpy as np
from insightface.app import FaceAnalysis
from insightface.app.common import Face
import onnxruntime
from PIL import Image
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(title="FaceSwap API")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create output directory if it doesn't exist
OUTPUT_DIR = Path("output")
OUTPUT_DIR.mkdir(exist_ok=True)

# Initialize face analysis
face_analyzer = FaceAnalysis(name='buffalo_l')
face_analyzer.prepare(ctx_id=-1, det_size=(640, 640))

# Load face swap model
model_path = "models/inswapper_128.onnx"
if not os.path.exists(model_path):
    logger.error(f"Face swap model not found at {model_path}")
    raise RuntimeError("Face swap model not found")

face_swapper = onnxruntime.InferenceSession(model_path)

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

def process_image(image_path: str) -> Optional[Face]:
    """Process image and return the first detected face."""
    img = cv2.imread(image_path)
    if img is None:
        raise ValueError("Failed to read image")
    
    faces = face_analyzer.get(img)
    if not faces:
        raise ValueError("No face detected in the image")
    
    return faces[0]

def process_video(video_path: str, source_face: Face, output_path: str):
    """Process video frames and apply face swap."""
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        raise ValueError("Failed to open video")

    # Get video properties
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    
    # Initialize video writer
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))
    
    frame_count = 0
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break
            
        # Process frame
        faces = face_analyzer.get(frame)
        if faces:
            # Apply face swap to the first detected face
            frame = face_swapper.run(None, {
                'source': source_face.embedding,
                'target': faces[0].embedding
            })[0]
        
        out.write(frame)
        frame_count += 1
        
        # Log progress
        if frame_count % 30 == 0:  # Log every 30 frames
            progress = (frame_count / total_frames) * 100
            logger.info(f"Processing video: {progress:.1f}% complete")
    
    cap.release()
    out.release()

@app.post("/faceswap")
async def face_swap(
    source_image: UploadFile = File(...),
    target_video: UploadFile = File(...)
):
    try:
        # Create temporary directory for processing
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_dir_path = Path(temp_dir)
            
            # Save uploaded files
            source_path = temp_dir_path / "source.jpg"
            video_path = temp_dir_path / "target.mp4"
            
            with open(source_path, "wb") as f:
                shutil.copyfileobj(source_image.file, f)
            with open(video_path, "wb") as f:
                shutil.copyfileobj(target_video.file, f)
            
            # Process source image
            logger.info("Processing source image...")
            source_face = process_image(str(source_path))
            
            # Generate output filename
            output_filename = f"output_{source_image.filename}_{target_video.filename}"
            output_path = OUTPUT_DIR / output_filename
            
            # Process video
            logger.info("Processing video...")
            process_video(str(video_path), source_face, str(output_path))
            
            logger.info("Face swap completed successfully")
            
            return JSONResponse({
                "status": "success",
                "output_path": str(output_path),
                "message": "Face swap completed successfully"
            })
            
    except Exception as e:
        logger.error(f"Error during face swap: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port) 