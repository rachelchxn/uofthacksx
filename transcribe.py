import requests
import time
import ffmpeg
from dotenv import load_dotenv

load_dotenv()

import os
key = os.environ.get("API_KEY_ASSEMBLYAI")

upload_endpoint = 'https://api.assemblyai.com/v2/upload'
transcript_endpoint = 'https://api.assemblyai.com/v2/transcript'

headers = {'authorization': key}

def upload(filename):
    def read_file(filename, chunk_size=5242880):
        with open(filename, 'rb') as _file:
            while True:
                data = _file.read(chunk_size)
                if not data:
                    break
                yield data
    response = requests.post(upload_endpoint,
                            headers=headers,
                            data=read_file(filename))
    audio_url = response.json()['upload_url']
    return audio_url


# transcribe

def transcribe(audio_url):
    transcript_request = { "audio_url": audio_url }
    transcript_response = requests.post(transcript_endpoint, json=transcript_request, headers=headers)

    job_id = transcript_response.json()['id']
    return job_id


# poll

def poll(transcript_id):
    polling_endpoint = transcript_endpoint + '/' + transcript_id
    polling_repsonse =  requests.get(polling_endpoint, headers=headers)
    return polling_repsonse.json()

def get_transcription_result_url(audio_url):
    transcript_id = transcribe(audio_url)
    while True:
        data =  poll(transcript_id)
        if data['status'] == 'completed':
            return data, None
        elif data['status'] == 'error':
            return data, data['error']
    
        time.sleep(5)

def save_transcript(audio_url, filename):
    data, error = get_transcription_result_url(audio_url)

    if data:
        transcript = data['text']
        return transcript
    elif error:
        return error







# import speech_recognition as sr

# def speechToText(file):
#     # initialize the recognizer
#     AUDIO_FILE = file
#     # use the audio file as the audio source                                        
#     r = sr.Recognizer()
#     with sr.AudioFile(AUDIO_FILE) as source:
#             audio = r.record(source)  # read the entire audio file                  

#             print("Transcription: " + r.recognize_google(audio))