# FaceSwap Adult

A professional face-swapping application for adult content, featuring a modern web interface and powerful backend processing.

## Project Structure

- `frontend/` - Next.js web application with Pornhub-inspired UI
- `backend/` - FastAPI server handling face-swapping operations

## Features

### Frontend
- Modern, responsive UI with Pornhub-inspired design
- Drag-and-drop file uploads
- Real-time progress tracking
- Error handling and user feedback

### Backend
- FastAPI server with face-swapping capabilities
- Support for image and video processing
- Efficient file handling
- Progress logging

## Tech Stack

### Frontend
- Next.js 14
- TypeScript
- Tailwind CSS
- React Dropzone
- React Icons

### Backend
- Python 3.9+
- FastAPI
- OpenCV
- InsightFace
- ONNX Runtime

## Getting Started

### Prerequisites
- Python 3.9 or higher
- Node.js 18 or higher
- Docker (optional)

### Backend Setup
1. Install Python dependencies:
```bash
pip install -r requirements.txt
```

2. Place the face swap model in the `models` directory:
```bash
mkdir -p models
# Place inswapper_128.onnx in the models directory
```

3. Start the backend server:
```bash
python main.py
```

### Frontend Setup
1. Navigate to the frontend directory:
```bash
cd frontend
```

2. Install dependencies:
```bash
npm install
```

3. Start the development server:
```bash
npm run dev
```

4. Open [http://localhost:3000](http://localhost:3000) in your browser.

## Deployment

### Backend
The backend can be deployed using Docker:
```bash
docker build -t faceswap-backend .
docker run -p 8000:8000 faceswap-backend
```

### Frontend
The frontend is configured for deployment on Vercel:
1. Connect your GitHub repository to Vercel
2. Set the environment variable `NEXT_PUBLIC_API_URL` to your backend URL
3. Deploy

## Environment Variables

### Frontend
```env
NEXT_PUBLIC_API_URL=http://localhost:8000
```

## License

MIT 