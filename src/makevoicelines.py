import openai


def createlines(inputgiven):
    openai.api_key_path = "openaikey.txt"

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": str(inputgiven)}
        ]
    )

    return completion.choices[0].message.content