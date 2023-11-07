import random

def check(input):
    if 'flip' in input:
        return True
    else:
        return False
    
def execute(input):
    choices = ['heads', 'tails']

    return f"The coin Landed {random.choice(choices)}"
