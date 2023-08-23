import speech_recognition as sr

def takeCommand():
     
    r = sr.Recognizer()
     
    with sr.Microphone() as source:
        
        r.adjust_for_ambient_noise(source)
        r.pause_threshold = 1
        audio = r.listen(source)  
    try:
        query = r.recognize_google(audio, language ='en-US')
    except:
        query = ""
    
    
    return query