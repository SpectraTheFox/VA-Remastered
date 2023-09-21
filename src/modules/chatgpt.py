import openai
import os
import dotenv

activation_options = ["what", "how", "when", "why"]

def check(input):
    if activation_options[0] in input or activation_options[1] in input or activation_options[2] in input or activation_options[3] in input:
        return True
    else: 
        return False
    
def execute(input):

    dotenv.load_dotenv()

    

    openai.api_key = os.environ['OAI_KEY']

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": input}
        ]
    )
    output = completion.choices[0].message.content
    print(output)
    return output