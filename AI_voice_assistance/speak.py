import pyttsx3


def say(text):
    engine=pyttsx3.init("sapi5")
    voices=engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate',170)
    print("     ")
    print(f"A.I : {text}")
    engine.say(text)
    engine.runAndWait()
    print("          ")

