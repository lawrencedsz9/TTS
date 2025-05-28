from TTS.api import TTS
import uuid
import torch
import logging
from pathlib import Path

logger = logging.getLogger(__name__)

class TTSService:
    def __init__(self):
        self.output_dir = Path("output")
        self.output_dir.mkdir(exist_ok=True)
        
        # Initialize TTS model
        try:
            self.model = TTS(
                model_name="tts_models/en/ljspeech/tacotron2-DDC",
                progress_bar=False,
                gpu=torch.cuda.is_available()
            )
            logger.info("TTS model loaded successfully")
        except Exception as e:
            logger.error(f"Failed to load TTS model: {str(e)}")
            raise

    def is_available(self) -> bool:
        """Check if the TTS service is available"""
        return hasattr(self, 'model') and self.model is not None

    def generate_speech(self, text: str) -> str:
        """Generate audio file and return its path"""
        try:
            filename = self.output_dir / f"{uuid.uuid4()}.wav"
            self.model.tts_to_file(text=text, file_path=str(filename))
            return str(filename)
        except Exception as e:
            logger.error(f"Error generating speech: {str(e)}")
            raise