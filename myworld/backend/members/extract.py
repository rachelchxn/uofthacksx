from .classify import *

def extract(input):
    prompt = f"""Sentence: Mitochondria are the powerhouses of the human body. They take fat, sugar, and protein from our food and combine it with oxygen to create energy for our cells and tissues such as brain and muscle, mitochondria have their own DNA that's crucial to this energy conversion process. This is different to the DNA found in the nucleus.
    
    Keyword: Mitochondria
    --
    Sentence: So, psychology is the scientific study of the mind, brain, and behaviour. 

    Keyword: Psychology
    --
    Sentence: DNA is it's a two-stranded polymer of nucleotides and each strand has a backbone made of identical sugar and phosphate groups with different nitrogenous bases pointing inwards, pairing in base specific manner, A with T and C with G. 
    
    Keyword: DNA
    --
    Sentence: {input}
    
    Keyword: """

    response = co.generate( 
        model='xlarge', 
        prompt = prompt,
        max_tokens=80, 
        temperature=1,
        stop_sequences=['--'])

    return response.generations[0].text

async def removify(preds, array):
    indices = [i for i, x in enumerate(preds) if x == "Remove"]

def keywordify(preds, array):
    indices_def = [i for i, x in enumerate(preds) if x == "Definition" or "Core Concept"]
    
    output = []
    for i in indices_def:
        output.append(array[int(i)])
    
    keywords = []
    for i in output:
        keywords.append(extract(i))
    indices_rem = [i for i, x in enumerate(preds) if x == "Remove"]
    
    output2 = array
    for i in indices_rem:
        output2.pop(i)
    
    return keywords, output2