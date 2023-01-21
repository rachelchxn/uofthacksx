from transcribe import *
from script import *
from classify import *
from testcohere import *
import re

# yt link 
filename = download_yt()

def transcribe(filename):
    audio_url = upload(filename)
    transcript = save_transcript(audio_url, filename)
    os.remove(filename)
    return transcript

transcript = transcribe(filename)


def splitter(prompt):
    span = 2
    a = prompt.split('. ')
    output = []
    for i in range(0, len(a), span):
       output.append(". ".join(a[i:i+span]))
    return output

transcript_array = splitter(transcript)

print(transcript)

for i in transcript_array:
    print(summarize(i))


# classifieds = classifyNotes(transcript_array)

# for i in transcript_array: 
#     print(i)

# print("predictions: ", classifieds)