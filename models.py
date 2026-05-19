from pydantic import BaseModel

class AudioFilesRequest(BaseModel):
    text: str
    voice: str = "en-US-JennyNeural"
    audio_file_name: str = "output"
    audio_file_type: str = "mp3"
    