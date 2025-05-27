from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import FileResponse
import uuid
from TTS.api import TTS

app = FastAPI()

# Load a pre-trained TTS model
tts = TTS(model_name="tts_models/en/ljspeech/tacotron2-DDC", progress_bar=False, gpu=False)

class TTSRequest(BaseModel):
    text: str

@app.post("/speak")
def text_to_speech(request: TTSRequest):
    # Generate unique filename
    filename = f"{uuid.uuid4()}.wav"
    
    # Convert text to speech and save to file
    tts.tts_to_file(text=request.text, file_path=filename)
    
    return FileResponse(path=filename, media_type="audio/wav", filename="output.wav")
