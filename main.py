from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from models import TTSRequest
from services.tts import TTSService
from services.email_service import EmailService
import logging
from pathlib import Path

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Create output directory
OUTPUT_DIR = Path("output")
OUTPUT_DIR.mkdir(exist_ok=True)

app = FastAPI()
tts_service = TTSService()
email_service = EmailService()

@app.post("/speak")
async def text_to_speech(request: TTSRequest):
    try:
        # Generate audio file
        filename = tts_service.generate_speech(request.text)
        
        # Send email with the audio file
        email_service.send_audio_email(
            to_email=request.email,
            audio_file_path=filename,
            text_content=request.text
        )
        
        # Return the audio file
        return FileResponse(
            path=filename,
            media_type="audio/wav",
            filename="output.wav"
        )
        
    except Exception as e:
        logger.error(f"Error: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))