import requests



def readlines(toread, outputnum):

    with open("elevenlabskey.txt",) as f:
        apikey = f.readline()

    CHUNK_SIZE = 1024
    url = "https://api.elevenlabs.io/v1/text-to-speech/QypdUQJPa9WOL0ENpPFn"

    headers = {
    "Accept": "audio/mpeg",
    "Content-Type": "application/json",
    "xi-api-key": apikey
    }

    data = {
    "text": toread,
    "model_id": "eleven_monolingual_v1",
    "voice_settings": {
        "stability": 1,
        "similarity_boost": 0.5
    }
    }

    response = requests.post(url, json=data, headers=headers)
    with open(f'output{outputnum}.mp3', 'wb') as f:
        for chunk in response.iter_content(chunk_size=CHUNK_SIZE):
            if chunk:
                f.write(chunk)