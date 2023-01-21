from transcribe import *
from script import *
from classify import *
import re

# yt link 
filename = download_yt()


def transcribe(filename):
    audio_url = upload(filename)
    transcript = save_transcript(audio_url, filename)
    os.remove(filename)
    return transcript


transcript = transcribe(filename)
array = transcript.split('. ')

classifieds = classify_notes(array)

for i in array: 
    print(i)

print("predictions: ", classifieds)