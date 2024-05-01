import pyttsx3
import datetime

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)
engine.setProperty("rate",200)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def greetMe():
    hour  = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("Good Morning,garv, i missed you")
    elif hour >12 and hour<=18:
        speak("Good Afternoon ,garv")

    else:
        speak("Good Evening,garv")
        speak("Please tell me, How can I help you ?")