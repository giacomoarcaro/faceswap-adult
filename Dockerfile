FROM python:3.9-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0 \
    wget \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy requirements first to leverage Docker cache
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Create models directory and download model
RUN mkdir -p models && \
    wget https://huggingface.co/facefusion/facefusion-models/resolve/main/inswapper_128.onnx -O models/inswapper_128.onnx

# Copy application code
COPY main.py .

# Create output directory
RUN mkdir -p output

# Expose port
EXPOSE 8000

# Run the application
CMD ["python", "main.py"] 