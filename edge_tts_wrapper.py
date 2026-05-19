import edge_tts
from .models import AudioFilesRequest

async def convert_text_to_audio_file(audioFilesRequest: AudioFilesRequest):
    audio_file_name = audioFilesRequest.audio_file_name + "." + audioFilesRequest.audio_file_type

    await (edge_tts
           .Communicate(audioFilesRequest.text, 
                        audioFilesRequest.voice)
           .save(audio_file_name))
    
    return audio_file_name + " was created."
