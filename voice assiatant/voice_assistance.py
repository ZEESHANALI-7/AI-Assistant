import os

import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import smtplib
import webbrowser
import sys
active = True
listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        talk("Good Morning mussu randi!")

    elif hour >= 12 and hour < 18:
        talk("Good Afternoon!")

    else:
        talk("Good Evening!")

    talk("hope your day is going good I am your virtual assistance  sir. Please tell me how may I help you")


wishMe()


def take_command():
    try:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print('listening...')
            r.pause_threshold = 1
            voice = r.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'google' in command:
                command = command.replace('google', '')
                print(command)
    except:
        pass
    return command


def run():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'yourself' in command:
        talk('I am a virtual assistance created by master zeeshan ali in the month of february. i can perform some simple task ike playing a song for you searching something for you etectra')
    elif 'created you' in command:
        talk('i was created by master zeeshan ali')
    elif "what can you do" in command:
        print("I can fulfill most of your requiments")
        talk("I can fulfill most of your requiments")
    elif "wikipedia" in command:
        talk("Searching wikipedia")
        command = command.replace('wikipedia', '')
        result = wikipedia.summary(command, sentences=2)
        talk("According to wikipedia")
        print(result)
        talk(result)
    elif 'tata' in command:
        talk('aryasamaego bye bye take care')
        sys.exit()
    elif 'code'in command:
       codepath = "C:\\Users\\zeesh\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code"
       os.startfile(codepath)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print('Current time is ' + time)
        talk('Current time is ' + time)
    elif "song for me" in command:
        talk("sorry i cant sing because i am very bat in singing songs")
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'want to go for a date' in command:
        talk('sorry, I have a headache')
    elif 'are you single' in command:
        talk('I am in a relationship with wifi')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'youtube' in command:
        webbrowser.open("youtube.com")
    elif 'google' in command:
        webbrowser.open("google.com")
    elif 'stackoverflow' in command:
        webbrowser.open("stackoverflow.com")
    else:
        talk('Please say the command again.')


while active:
    run()

