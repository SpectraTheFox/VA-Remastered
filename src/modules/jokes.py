import random

jokes = []

def check(input):
    if 'joke' in input: 
        return True
    else:
        return False

def execute(input):
    with open('jokes.txt', 'r') as jokefile:
        lines = jokefile.readlines()
        for line in lines:
            jokes.append(line)

    return random.choice(jokes)