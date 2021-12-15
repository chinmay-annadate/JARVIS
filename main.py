"""
Created on Tue Jan 12 18:10:00 2021

@author: Chinmay Annadate

Jarvis Virtual Assistant
"""

import pyttsx3
import datetime
import speech_recognition
import wikipedia
import webbrowser
import os

# text to speech conversion
engine = pyttsx3.init('sapi5')


# speak function
def speak(text):
    engine.say(text)
    engine.runAndWait()


# my functions
def functions():
    out = "Hello there, my functions include telling time, opening file explorer, wikipedia searches, opening youtube, opening google, playing music, opening google chrome"
    print(out)
    speak(out)


# greetings
def greetings():
    H = int(datetime.datetime.now().hour)
    if 0 <= H < 12:
        zone = "morning"

    elif 12 <= H < 17:
        zone = "afternoon"
        
    elif 17 <= H < 0:
        zone = "evening"
    
    out = f"Good {zone} sir, how may I be of assistance?"
    print(out)
    speak(out)


# introduction
def introduction():
    out = "Hello, I'm Jarvis, your personal virtual assistant. Jarvis stands for just a rather very intelligent assistant. I am here to help you in various tasks. Ask what can you do to know my functions"
    print(out)
    speak(out)


# command
def command():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception:
        print("Voice unclear, please try again")
        return "None"
    return query


greetings()
while True:
    query = command().lower()

    # functions
    if 'what can you do' in query:
        functions()

    # wikipedia search
    elif "wikipedia" in query:
        speak("Searching in wikipedia..")
        query = query.replace("wikipedia", "")
        search_result = wikipedia.summary(query, sentences=2)
        print(search_result)
        speak(search_result)

    # youtube
    elif "open youtube" in query:
        print("opening youtube")
        webbrowser.open("youtube.com")

    # google
    elif "open google" in query:
        print("google")
        webbrowser.open("google.com")

    # music
    elif "play music" in query:
        dir = 'F:\\ae dil hai mushkil songs'
        songs = os.listdir(dir)
        print(songs)
        os.startfile(os.path.join(dir, songs[0]))

    # know time
    elif 'the time' in query:
        toime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"It's {toime}")
        print(f"It's {toime}")

    # introduction
    elif 'who are you' in query:
        introduction()

    # this pc
    elif 'this pc' in query:
        codePath = "This PC"
        print("opening this pc")
        os.startfile(codePath)

    # open chrome
    elif 'google chrome' in query:
        codePath = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
        print("opening google chrome")
        os.startfile(codePath)

    # open my drive
    elif 'my drive' in query:
        print("opening your drive")
        codePath = "D:\\"
        os.startfile(codePath)
        
    # exiting
    elif 'that will be all' in query:
        output = "good night sir"
        print(output)
        speak(output)
        break
    
    # invalid command
    else:
        speak('invalid command')
        print('invalid command')
