import voice as voice
import makevoicelines as lines
import listen as listen
from pygame import mixer  # Load the popular external library
import time
mixer.init()


keepgoing = True
outputnumber = 0
while keepgoing:
    wakeup = listen.takeCommand()
    if "prism" in wakeup:
        voice.readlines("what can I do for you sir?", outputnumber)
        mixer.music.load(f'output{outputnumber}.mp3')
        mixer.music.play()
        while mixer.music.get_busy():  # wait for music to finish playing
            time.sleep(1)
        mixer.music.stop()
        outputnumber += 1
        whatinput = listen.takeCommand()
        print(whatinput)
        toread = lines.createlines(whatinput)
        voice.readlines(toread, outputnumber)
        mixer.music.load(f'output{outputnumber}.mp3')
        mixer.music.play()
        while mixer.music.get_busy():  # wait for music to finish playing
            time.sleep(1)
        mixer.music.stop()
        outputnumber += 1
        keepgoing = False
        