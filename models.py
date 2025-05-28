from pydantic import BaseModel, EmailStr

class TTSRequest(BaseModel):
    text: str
    email: EmailStr
