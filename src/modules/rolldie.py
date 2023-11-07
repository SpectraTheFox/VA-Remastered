import random

def check(input):
    if 'roll' in input: 
        return True
    else:
        return False

def execute(input):
    return f"You rolled a {random.randint(1,6)}"