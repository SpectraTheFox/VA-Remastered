import voice as voice
import listen
import os
import importlib


moduleslist = []
for (dirpath, dirnames, filenames) in os.walk("src\modules"):
    moduleslist.extend(filenames)
    break
moduleslist = [x.replace(".py", "") for x in moduleslist]
print(moduleslist)

keepgoing = True
outputnumber = 0
while keepgoing:
    print("waiting for wakeup")
    wakeup = listen.takeCommand()
    print("input: " + wakeup)
    
    if "prism" in wakeup or "Prism" in wakeup:
        voice.readlines("what can I do for you", outputnumber)
        outputnumber += 1
        print("waiting for command")
        promptgiven = listen.takeCommand()
        print("input: " + promptgiven)
        
        for item in moduleslist:
            module = importlib.import_module(f"modules.{item}")
            
            if module.check(promptgiven):
                print(item)
                toread = module.execute(promptgiven)
                voice.readlines(toread, outputnumber)
                outputnumber += 1
        
        
        