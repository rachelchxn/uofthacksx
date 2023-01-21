from transcribe import *
from script import *


def transcribe():
    filename = download_yt()
    audio_url = upload(filename)
    transcript = save_transcript(audio_url, filename)
    os.remove(filename)
    return transcript

transcript = transcribe()

print(transcript)