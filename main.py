from transcribe import *
from script import *
from classify import *
from extract import *

#youtube = CoolClass()

#filename = youtube.download_yt()

def transcribe(filename):
    audio_url = upload(filename)
    transcript = save_transcript(audio_url, filename)
    os.remove(filename)
    return transcript

#transcript = transcribe(filename)


def splitter(prompt):
    span = 3
    a = prompt.split('. ')
    output = []
    for i in range(0, len(a), span):
       output.append(". ".join(a[i:i+span]))
    return output

#transcript = "Our bodies run on energy. Even as you sit watching this, your body is generating enough energy to power 710 watt light bulbs. Most of that energy is provided by tiny structures called mitochondria present inside our cells. These mitochondria are the powerhouses of a human body. They take fat, sugar, and protein from our food and combine it with oxygen oxygen, converting it into energy for our cells and tissues such as brain and muscle, mitochondria have their own DNA that's crucial to this energy conversion process. This is different to the DNA found in the nucleus. While nuclear DNA determines our physical characteristics, mitochondrial DNA does not. But both types of DNA must be healthy for the mitochondria to function effectively. Faults in either can cause mitochondria to stop working properly, preventing them from converting fuel into energy. If the number of 40 mitochondria reaches a critical level, our cells begin to run out of energy, fail, and even die. Since mitochondria performs so many different functions, there are literally hundreds of different mitochondrial diseases. The effects include fatigue, speech disorders, hearing difficulties, muscle weakness, heart problems, liver disease, bowel problems, and sometimes, in very severe cases, it may even be fatal. The sheer variety of symptoms associated with mitochondrial disease makes it hard to diagnose. Despite this, we're making rapid advances every day in our understanding of how it develops and is passed on. All of which help us to devise new strategies to prevent and treat the disease in the future. To learn more about mitochondrial disease, please visit our website."

#transcript_array = splitter(transcript)


summarized_array = ['Our bodies run on energy. Even as you sit watching this, your body is generating enough energy to power 710 watt light bulbs. Most of that energy is provided by tiny structures called mitochondria present inside our cells.', "These mitochondria are the powerhouses of a human body. They take fat, sugar, and protein from our food and combine it with oxygen oxygen, converting it into energy for our cells and tissues such as brain and muscle, mitochondria have their own DNA that's crucial to this energy conversion process.", "This is different to the DNA found in the nucleus. While nuclear DNA determines our physical characteristics, mitochondrial DNA does not. But both types of DNA must be healthy for the mitochondria to function effectively.", "Faults in either can cause mitochondria to stop working properly, preventing them from converting fuel into energy.", 'If the number of 40 mitochondria reaches a critical level, our cells begin to run out of energy, fail, and even die. Since mitochondria performs so many different functions, there are literally hundreds of different mitochondrial diseases.', 'The effects include fatigue, speech disorders, hearing difficulties, muscle weakness, heart problems, liver disease, bowel problems, and sometimes, in very severe cases, it may even be fatal.', "The sheer variety of symptoms associated with mitochondrial disease makes it hard to diagnose. Despite this, we're making rapid advances every day in our understanding of how it develops and is passed on. All of which help us to devise new strategies to prevent and treat the disease in the future.", "To learn more about mitochondrial disease, please visit our website."]
def sum_array(summarized_array):
    summarized_array = []
    for i in transcript_array:
        summarized_array.append(summarize(i))
    return summarized_array

#summarized_array = sum_array(transcript_array)

classifieds = classifyNotes(summarized_array)


keywords = list(dict.fromkeys(keywords(classifieds, summarized_array)))

class_notes = []

for i in summarized_array:
    class_notes.append([classifieds[summarized_array.index(i)], i])

print(class_notes)
print('keywords', keywords)