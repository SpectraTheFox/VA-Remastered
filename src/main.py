import voice as voice
import listen
import os
import importlib
import random 

introslist = []

moduleslist = []
for (dirpath, dirnames, filenames) in os.walk("src/modules"):
    moduleslist.extend(filenames)
    break
moduleslist = [x.replace(".py", "") for x in moduleslist]
moduleslist.remove(".DS_Store")
print(moduleslist)

textorvoice= input("Do You Want Voice or Text Input?\n")

def va_input():
    if textorvoice == "Voice" or textorvoice == "voice":
       return listen.takeCommand()
    elif textorvoice == "Text" or textorvoice == "text": 
        return input("Input: ")

keepgoing = True
outputnumber = 0
while keepgoing:
    print("waiting for wakeup")
    wakeup = va_input()
    with open("src/intros.txt", "r") as intosfile:
        intros = intosfile.readlines()
        for lines in intros:
            introslist.append(lines)
    
    if "prism" in wakeup or "Prism" in wakeup:
        voice.readlines(random.choice(introslist), outputnumber)
        outputnumber += 1
        print("waiting for command")
        promptgiven = va_input()
        
        for item in moduleslist:
            module = importlib.import_module(f"modules.{item}")
            
            if module.check(promptgiven):
                print(item)
                toread = module.execute(promptgiven)
                voice.readlines(toread, outputnumber)
                outputnumber += 1 
        
        