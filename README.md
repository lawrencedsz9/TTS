# Text-to-Speech with Email Service

A FastAPI application that converts text to speech and sends the audio file via email.

## Features

- Text-to-speech conversion using Coqui TTS
- Email delivery using Gmail SMTP
- Automatic file cleanup

1. Create and activate virtual environment:

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create `.env` file in the project root:
```
GMAIL_USERNAME=your.email@gmail.com
GMAIL_APP_PASSWORD=your_16_character_app_password
```

## Usage

1. Start the server:
```bash
uvicorn main:app --reload
```

2. The API will be available at `http://localhost:8000`

3. Send a POST request to `/speak` endpoint:
```json
{
    "text": "Text to convert to speech",
    "email": "recipient@example.com"
}
