# Face Swap API

A FastAPI-based backend service for face swapping in videos using deep learning models.

## Features

- Face detection and extraction from source images
- Face swapping in video frames
- Progress tracking and logging
- Temporary file handling
- Docker support

## Prerequisites

- Python 3.9 or higher
- Docker (optional, for containerized deployment)
- Face swap model file (`inswapper_128.onnx`)

## Setup

1. Clone the repository
2. Create a `models` directory and place the face swap model file (`inswapper_128.onnx`) in it
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running Locally

1. Start the server:
   ```bash
   python main.py
   ```
   The server will start at `http://localhost:8000`

2. Use Docker:
   ```bash
   docker build -t faceswap-api .
   docker run -p 8000:8000 faceswap-api
   ```

## API Endpoints

### Health Check
- **GET** `/health`
- Returns the server status

### Face Swap
- **POST** `/faceswap`
- Accepts multipart form data with:
  - `source_image`: Source face image (JPG/PNG)
  - `target_video`: Target video file (MP4)
- Returns JSON response with output video path

## Example Usage

Using curl:
```bash
curl -X POST "http://localhost:8000/faceswap" \
  -H "accept: application/json" \
  -H "Content-Type: multipart/form-data" \
  -F "source_image=@path/to/source.jpg" \
  -F "target_video=@path/to/target.mp4"
```

## Output

Processed videos are saved in the `output` directory with filenames in the format:
`output_[source_image_name]_[target_video_name]`

## Notes

- The application uses temporary storage for processing files
- All temporary files are automatically deleted after processing
- Progress is logged to the console during video processing
- The face swap model must be placed in the `models` directory before running 