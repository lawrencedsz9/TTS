# Text-to-Speech API

A FastAPI-based web service that converts text to speech using the Coqui TTS library.

## Features

- RESTful API endpoint for text-to-speech conversion
- Uses LJSpeech model with Tacotron2-DDC architecture
- GPU acceleration support
- Returns WAV audio files

## Prerequisites

- Python 3.7+
- NVIDIA GPU with CUDA support (for GPU acceleration)
- CUDA drivers installed
- PyTorch with CUDA support

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd <repository-name>
```

2. Install the required dependencies:
```bash
pip install fastapi uvicorn TTS pydantic
```

## Usage

1. Start the server:
```bash
uvicorn main:app --reload
```

2. The API will be available at `http://localhost:8000`

3. Send a POST request to `/speak` endpoint:
```bash
curl -X POST "http://localhost:8000/speak" \
     -H "Content-Type: application/json" \
     -d '{"text": "Hello, this is a test."}'
```

The response will be a WAV audio file containing the synthesized speech.

## API Documentation

### POST /speak

Converts text to speech and returns an audio file.

**Request Body:**
```json
{
    "text": "Text to convert to speech"
}
```

**Response:**
- Content-Type: audio/wav
- File: output.wav

## GPU Acceleration

The service is configured to use GPU acceleration by default. To verify GPU support:

1. Check if CUDA is available:
```python
import torch
print(torch.cuda.is_available())
```

2. Monitor GPU usage:
```bash
nvidia-smi
```

## License

[Add your license information here]

## Contributing

[Add contribution guidelines here]
