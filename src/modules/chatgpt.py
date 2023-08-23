import openai

def check(input):
    if "what" in input:
        return True
    else: 
        return False
    
def execute(input):

    openai.api_key_path = "openaikey.txt"

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": input}
        ]
    )
    return completion.choices[0].message.content