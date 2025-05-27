# Text-to-Speech API

A FastAPI-based web service that converts text to speech using the Coqui TTS library.

## Features

- RESTful API endpoint for text-to-speech conversion
- Uses LJSpeech model with Tacotron2-DDC architecture
- GPU acceleration support
- Returns WAV audio files

## Installation

1. Clone the repository:


2. Install the required dependencies:
pip install -r requirements.txt

## Usage

1. Start the server:
```bash
uvicorn main:app --reload
```

2. The API will be available at `http://localhost:8000`

3. Send a POST request to `/speak` endpoint:

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
