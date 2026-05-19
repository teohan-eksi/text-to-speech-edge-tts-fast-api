from .main import app
from .edge_tts_wrapper import convert_text_to_audio_file
from .models import AudioFilesRequest

@app.post("/audio-files")
async def call_convert_text_to_audio_file(audioFilesRequest: AudioFilesRequest): 
    return await convert_text_to_audio_file(audioFilesRequest)
