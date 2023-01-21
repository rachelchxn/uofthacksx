from testcohere import *

from cohere.classify import Example

a = 'main concept'
b = 'point'
c = 'example'



examples=[
  Example("So now moving onto functions", a),
  Example("Let's talk a bit more about the mitochondria", a),
  Example("Speaking of the industrial revolution", a),
  Example("Next, we'll talk about the theory by John Smith", a),
  Example("Taking a look at the next topic", a),
  Example("We will first discuss how to design an interface", a),

  Example("One of the functions of a mitochodrion is to generate energy", b),
  Example("An important note about functions is that they pass the vertical line test", b),
  Example("In 1980, the most important moment of the industrial revolution took place", b),
  Example("The theory was developed first by John Smith", b),
  Example("This topic is important for your midterm exam", b),
  Example("To design interfaces, we need to pay attention to user experience", b),
  
  Example("For example, the mitochodrion uses energy from ATP", c),
  Example("An example of a graph of a non-function is shown here", c),
  Example("The industrial revolution is an example of an important era", c),
  Example("John Smith is an example of an important theorist", c),
  Example("This topic is one of the topics that will appear on your midterm exam", c),
  Example("i.e. The user experience", c)
]

def classifyNotes(input):
    response = co.classify(
        model='large',  
        inputs=input,  
        examples=examples
        )
    preds = []
    for i in response.classifications:
        preds.append(i.prediction)
    return preds

# use csv to give a lot of data

def summarize(input):
    prompt = f"""Passage: Alright, so the world has seemingly become utterly divided on this dress. What colours do you see? On one side we have team Black and Blue - on the other, team White and Gold.
    TLDR: People disagree on the colour of this dress; some see Black and Blue, others see White and Gold
    --
    Passage: We asked on twitter and got hundreds of responses for both white and gold and black and blue. For what it’s worth, we both saw black and blue and thought this was a massive prank at first. So how can it be possible for people to see it so differently? It’s a phenomenon known as colour constancy.
    TLDR: What worth seemed like a prank at first turned out to be a display of a phenomenon known as colour constancy.
    --
    Passage: Take this cube for example. The middle square on the top appears to be a shade of brown, while the one on the side looks much more orange. But in actuality, they are both the exact same colour. We promise we haven’t cheated here or done any trick photography.
    TLDR: For example, middle square on the top of this cube appears to be a shade of brown, while the one on the side looks much more orange, but they are actually the same colour.
    --
    Passage: {input}
    TLDR: """
    response = co.generate( 
        model='xlarge', 
        prompt = prompt,
        max_tokens=40, 
        temperature=0.8,
        stop_sequences=["--"])

    return response.generations[0].text
