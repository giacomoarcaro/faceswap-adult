'use client';

import { useState } from 'react';
import { useDropzone } from 'react-dropzone';
import { FiUpload, FiLoader } from 'react-icons/fi';

const API_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000';

export default function Home() {
  const [sourceImage, setSourceImage] = useState<File | null>(null);
  const [targetVideo, setTargetVideo] = useState<File | null>(null);
  const [isProcessing, setIsProcessing] = useState(false);
  const [resultUrl, setResultUrl] = useState<string | null>(null);
  const [error, setError] = useState<string | null>(null);

  const onSourceDrop = (acceptedFiles: File[]) => {
    if (acceptedFiles[0]?.type.startsWith('image/')) {
      setSourceImage(acceptedFiles[0]);
      setError(null);
    } else {
      setError('Please upload a valid image file');
    }
  };

  const onTargetDrop = (acceptedFiles: File[]) => {
    if (acceptedFiles[0]?.type.startsWith('video/')) {
      setTargetVideo(acceptedFiles[0]);
      setError(null);
    } else {
      setError('Please upload a valid video file');
    }
  };

  const sourceDropzone = useDropzone({
    onDrop: onSourceDrop,
    accept: {
      'image/*': ['.png', '.jpg', '.jpeg']
    },
    maxFiles: 1
  });

  const targetDropzone = useDropzone({
    onDrop: onTargetDrop,
    accept: {
      'video/*': ['.mp4']
    },
    maxFiles: 1
  });

  const handleSwap = async () => {
    if (!sourceImage || !targetVideo) return;

    setIsProcessing(true);
    setError(null);
    const formData = new FormData();
    formData.append('source_image', sourceImage);
    formData.append('target_video', targetVideo);

    try {
      const response = await fetch(`${API_URL}/faceswap`, {
        method: 'POST',
        body: formData,
      });

      if (!response.ok) {
        throw new Error('Failed to process files');
      }

      const data = await response.json();
      if (data.status === 'success') {
        setResultUrl(data.output_path);
      } else {
        throw new Error(data.message || 'Failed to process files');
      }
    } catch (error) {
      console.error('Error processing files:', error);
      setError(error instanceof Error ? error.message : 'An error occurred');
    } finally {
      setIsProcessing(false);
    }
  };

  return (
    <main className="container mx-auto px-4 py-8">
      {/* Logo */}
      <div className="text-center mb-12">
        <h1 className="logo-text">MyBestOne</h1>
      </div>

      {/* Upload Boxes */}
      <div className="grid grid-cols-1 md:grid-cols-2 gap-8 mb-12">
        {/* Source Image Upload */}
        <div
          {...sourceDropzone.getRootProps()}
          className={`upload-box ${sourceDropzone.isDragActive ? 'border-ph-orange bg-gray-900' : ''}`}
        >
          <input {...sourceDropzone.getInputProps()} />
          <FiUpload className="mx-auto h-12 w-12 mb-4" />
          <p className="text-lg mb-2">Upload Source Face</p>
          <p className="text-sm text-gray-400">Drag & drop or click to select</p>
          {sourceImage && (
            <p className="text-sm text-ph-orange mt-2">{sourceImage.name}</p>
          )}
        </div>

        {/* Target Video Upload */}
        <div
          {...targetDropzone.getRootProps()}
          className={`upload-box ${targetDropzone.isDragActive ? 'border-ph-orange bg-gray-900' : ''}`}
        >
          <input {...targetDropzone.getInputProps()} />
          <FiUpload className="mx-auto h-12 w-12 mb-4" />
          <p className="text-lg mb-2">Upload Target Video</p>
          <p className="text-sm text-gray-400">Drag & drop or click to select</p>
          {targetVideo && (
            <p className="text-sm text-ph-orange mt-2">{targetVideo.name}</p>
          )}
        </div>
      </div>

      {/* Error Message */}
      {error && (
        <div className="text-center mb-4">
          <p className="text-red-500">{error}</p>
        </div>
      )}

      {/* Swap Button */}
      <div className="text-center mb-8">
        <button
          onClick={handleSwap}
          disabled={!sourceImage || !targetVideo || isProcessing}
          className="swap-button"
        >
          {isProcessing ? (
            <span className="flex items-center justify-center">
              <FiLoader className="animate-spin mr-2" />
              Processing...
            </span>
          ) : (
            'Make the Swap'
          )}
        </button>
      </div>

      {/* Result */}
      {resultUrl && (
        <div className="text-center">
          <p className="text-xl mb-4">Video ready!</p>
          <a
            href={resultUrl}
            download
            className="text-ph-orange hover:underline"
          >
            Download Result
          </a>
        </div>
      )}
    </main>
  );
} 