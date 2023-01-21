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

def classify_notes(input):
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