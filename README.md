# Text-to-Speech with Email Service

A FastAPI application that converts text to speech and sends the audio file via email.

## Features

- Text-to-speech conversion using Coqui TTS
- Email delivery using Gmail SMTP
- Automatic file cleanup
- Health check endpoint

## Setup

1. Clone the repository:
```bash
git clone <repository-url>
cd <repository-name>
```

2. Create and activate virtual environment:
```bash
python -m venv venv
# On Windows:
.\venv\Scripts\activate
# On Unix/MacOS:
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up Gmail App Password:
   - Go to your Google Account settings
   - Enable 2-Step Verification if not already enabled
   - Go to Security → App Passwords
   - Select "Mail" as the app and "Other" as the device
   - Copy the generated 16-character password

5. Create `.env` file in the project root:
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
```

4. Check service health:
```bash
curl http://localhost:8000/health
```

## API Documentation

- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Project Structure

```
.
├── .env                  # Gmail configuration
├── main.py              # FastAPI application
├── models.py            # Data models
├── requirements.txt     # Dependencies
├── services/
│   ├── tts.py          # Text-to-Speech service
│   └── email_service.py # Gmail email service
└── output/             # Directory for generated audio files
```
