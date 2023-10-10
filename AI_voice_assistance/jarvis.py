import random
import json
import torch
from brain import Neural_Network
from NeuralNetwork import bag_of_words, tokenize

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
with open("intents.json", 'r') as json_data:
    intents = json.load(json_data)

FILE = "TrainData.pth"
data = torch.load(FILE)

input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data["all_words"]
tags = data["tags"]
model_state = data["model_state"]

model = Neural_Network(input_size, hidden_size, output_size).to(device)
model.load_state_dict(model_state)
model.eval()

# ***************************************************************
Name = "friday"
from listen import Listen
from speak import say
from task import NonInputExecution
from task import InputExecution


def main():
    sentence = Listen()
    result=str(sentence)
    if sentence == "bye":
        exit()
    sentence = tokenize(sentence)
    
    X = bag_of_words(sentence, all_words)
    X = X.reshape(1, -1)
    X = torch.from_numpy(X).to(device)

    output = model(X)
    _, predicted = torch.max(output, dim=1)
    predicted = predicted.item()

    tag = tags[predicted]

    probs = torch.softmax(output, dim=1)
    prob = probs[0][predicted]

    if prob.item() > 0.8:
        for intent in intents['intents']:
            if tag == intent["tag"]:
                reply = random.choice(intent['responses'])
                if "time" in reply:
                    NonInputExecution(reply)
                elif "date" in reply:
                    NonInputExecution(reply)
                elif "day" in reply:
                    NonInputExecution(reply)


                elif "wikipedia" in reply:
                    InputExecution(reply,result)  
                elif "meaning" in reply:
                    InputExecution(reply,result)
                elif "google" in reply:
                    InputExecution(reply,result)
                elif "youtube" in reply:
                    InputExecution(reply,result)
                elif "any" in reply:
                    InputExecution(reply,result)
                elif "screenshot" in reply:
                    InputExecution(reply,result)
                elif "stop" in reply:
                    InputExecution(reply,result)
                elif "play" in reply:
                    InputExecution(reply,result)
                elif "full screen" in reply:
                    InputExecution(reply,result)
                elif "skip" in reply:
                    InputExecution(reply,result)
                elif "back" in reply:
                    InputExecution(reply,result)
                elif "restart" in reply:
                    InputExecution(reply,result)
                else:
                     say(reply)

while True:
     main()
