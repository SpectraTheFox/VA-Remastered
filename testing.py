import openai
import os

inputgiven = input("What are you asking?\n")

openai.api_key_path = "openaikey.txt"

completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": inputgiven}
    ]
)

print(completion.choices[0].message.content)