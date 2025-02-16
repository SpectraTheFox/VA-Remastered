from datetime import datetime

def check(input):
    if 'time' in input:
        return True
    else:
        return False

def execute(input):
    return datetime.now().strftime('%H:%M:%S')
