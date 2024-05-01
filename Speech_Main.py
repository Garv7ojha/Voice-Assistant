import pyttsx3
import speech_recognition
import setuptools
import requests
from bs4 import BeautifulSoup
import datetime
import os
import pyautogui

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)
rate = engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source,0,4)

    try:
        print("Understanding..")
        query  = r.recognize_google(audio,language='en-in')
        print(f"You Said: {query}\n")
    except Exception as e:
        print("Say that again")
        return "None"
    return query


      

if __name__ == "__main__":
    while True:
        query = takeCommand().lower()
        if "wake up" in query:
            from greetMe import greetMe
            greetMe()

            while True:
                query = takeCommand().lower()
                if "go to sleep" in query:
                    speak("Ok garv , You can call me anytime")
                    break
#######################################################################################################################################          
            
                elif "hello" in query:
                    speak("Hello garv, how are you ?")
                elif "i am fine" in query:
                    speak("that's great, garv") 
                elif "how are you" in query:
                    speak("Perfect, garv")
                    
                elif "thank you" in query:
                    speak("you are welcome, garv")

                elif"open" in query:
                    from Dictapp import openappweb 
                    openappweb(query)
                elif "close" in query:
                    from Dictapp import closeappweb
                    closeappweb(query)
#####################################################################################################################################
                elif"pause" in query:
                    pyautogui.press("k")
                    speak("video paused")
                elif "play" in query:
                    pyautogui.press("k")
                    speak("video played")
                elif "mute" in query:
                    pyautogui.press("m")
                    speak("video muted")

                elif "volume up" in query:
                    from Keyboard import volumeup
                    speak("Turning volume up,Garv")
                    volumeup()
                elif "volume down" in query:
                    from Keyboard import volumedown
                    speak("Turning volume down, Garv")
                    volumedown()
########################################################################################################################################
                elif "google" in query: 
                    from SearchNow import searchGoogle
                    searchGoogle(query)
                elif "youtube" in query:
                    from SearchNow import searchYoutube
                    searchYoutube(query)
                elif "wikipedia" in query:
                    from SearchNow import searchWikipedia
                    searchWikipedia(query)
######################################################################################################################################
                elif "news" in query:
                    from NewsRead import latestnews
                    latestnews()

####################################################################################################################################### 
                elif "temperature today" in query:
                    search = "temperature in delhi"
                    url = f"https://www.google.com/search?q={search}"
                    r  = requests.get(url)
                    data = BeautifulSoup(r.text,"html.parser")
                    temp = data.find("div", class_ = "BNeawe").text
                    speak(f"current{search} is {temp}")
#######################################################################################################################################
                elif "weather today" in query:
                    search = "temperature in delhi"
                    url = f"https://www.google.com/search?q={search}"
                    r  = requests.get(url)
                    data = BeautifulSoup(r.text,"html.parser")
                    temp = data.find("div", class_ = "BNeawe").text
                    speak(f"current{search} is {temp}")
######################################################################################################################################
                elif "the time" in query: 
                    strTime = datetime.datetime.now().strftime("%H:%M")    
                    speak(f"garv, the time is {strTime}")

                elif"what is the time" in query:
                     strTime = datetime.datetime.now().strftime("%H:%M")    
                     speak(f"garv, the time is {strTime}")

                elif"tell me what is the time" in query:
                    strTime = datetime.datetime.now().strftime("%H:%M")    
                    speak(f"garv, the time is {strTime}")
#####################################################################################################################################
                
                elif "sleep" in query:
                    speak("ok garv love you, bye byee")
                    exit()
#####################################################################################################################################
               
                elif "open" in query:
                    from Dictapp import openappweb
                    openappweb(query)
                elif "close" in query:
                     from Dictapp import closeappweb
                     closeappweb(query)
#####################################################################################################################################
                elif "remember that" in query:
                    rememberMessage = query.replace("remember that","")
                    rememberMessage = query.replace("jarvis","")
                    speak("You told me to "+rememberMessage)
                    remember = open("Remember.txt","a")
                    remember.write(rememberMessage)
                    remember.close()

                elif "what do you remember" in query:
                    remember = open("Remember.txt","r")
                    speak("You told me to " + remember.read())
######################################################################################################################################
















#######################################################################################################################################
                elif "shutdown the system" in query:
                    speak("Are You sure you want to shutdown")
                    shutdown = input("Do you wish to shutdown your computer? (yes/no)")
                    if shutdown == "yes":
                        os.system("shutdown /s /t 1")

                    elif shutdown == "no":
                        break

              