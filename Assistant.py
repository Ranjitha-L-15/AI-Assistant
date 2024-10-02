import time
from datetime import datetime
from random import choice

import pyautogui
import pyttsx3
import speech_recognition as sr
import os
import cv2
import random
from requests import get
import wikipedia
import webbrowser
import pywhatkit as kit
import smtplib
import pyjokes
import sys

engine = pyttsx3.init('sapi5')
engine.setProperty('volume', 2.0)
engine.setProperty('rate', 225)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

USER = "Ranjitha"
HOSTNAME = "ray"


def speak(text):
    engine.say(text)
    engine.runAndWait()


def greet_me():
    hour = datetime.now().hour
    if (hour >= 6) and (hour < 12):
        speak(f"Good Morning {USER}")
    elif (hour >= 12) and (hour < 16):
        speak(f"Good Afternoon {USER}")
    elif (hour >= 16) and (hour < 19):
        speak(f"Good Evening {USER}")
    elif (hour > 19) and (hour < 24):
        speak(f"Good Night {USER}")
    elif (hour >= 1) and (hour < 4):
        speak(f"Hey why didn't you sleep yet {USER}")

    speak(f"I'm {HOSTNAME} , How can I assist you? {USER}")


def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening......")
        r.pause_threshold = 1
        audio = r.listen(source)

    #
    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print(f"USER SAID:- {query}")

    except Exception as e:
        speak("Sorry I couldn't understand, could you please repeat again?")
        query = 'None'

    return query

def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('1nt21ec111.ranjitha@nmit.ac.in','(Gwt_My@)')
    server.sendmail('1nt21ec111.ranjitha@nmit.ac.in',to,content)
    server.close()


if __name__ == '__main__':
    # speak("Hey there, I'm your virtual assistant")
    # print("Hey there,I'm your virtual assistant")
    greet_me()
    take_command()

    while True:   # while True: (infinite loop)
    # if 1:  # if 1: (executes once)
        query = take_command().lower()

        #Building logic to perfrm a task

        if 'open notepad' in query:
            npath = 'C:\\Windows\\notepad.exe'
            os.startfile(npath)
        elif 'open zoom meeting' in query:
            zpath = 'C:\\Users\\hp\\AppData\\Roaming\\Zoom\\bin\\zoom.exe'
            os.startfile(zpath)
        elif 'open command prompt' in query:
            os.system('start cmd')
        elif 'open Microsoft Edge' in query:
            os.system('start Microsoft Edge')
        elif 'open camera' in query:  # To open Camera
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow('webcam', img)
                k = cv2.waitKey(50)
                if k == 27:
                    break;
            cap.release()
            cv2.destroyAllWindows()
        elif 'play music' in query:  # To play music
            music_dir = "C:\\music"
            songs = os.listdir(music_dir)
            rd = random.choice(songs)
            os.startfile(os.path.join(music_dir, rd))
        elif 'ip address' in query:
            ip = get('https://api.ipify.org').text
            speak(f"Your ip address is:- {ip}")
            print(ip)

        elif "wikipedia" in query:
            speak("Searching wikipedia.....")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("according to wikipedia")
            speak(results)
            print(results)
        elif "open youtube" in query:
            webbrowser.open("www.youtube.com")
        elif "open google" in query:
            speak("sweetheart, what should I search on google for you")
            cm = take_command().lower()
            chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(chrome_path).open(f"https://www.google.com/search?q={cm}")
            # webbrowser.open(cm)
        elif "send message" in query:
            kit.sendwhatmsg("+918217596649","This is a testing protocol",12,2)
        elif "play songs on youtube" in query:
            kit.playonyt("SOLO")         # kit.playonyt() is used to play songs on youtube

        elif 'email to ranjitha' in query:
            try:
                speak("What should I say")
                content = take_command().lower()
                to = "ranjithal1516@gmail.com"
                sendEmail(to,content)
                speak("Email has been sent to ranjitha")

            except Exception as e:
                print(e)
                speak("Sorry darling, I'm not able to send this email to ranjitha")


    #To close any application
        elif "Close notepad" in query:
            speak("okay babe,closing notepad")
            os.system("taskkill /f /im notepad.exe")

    # To set an alarm
        elif "Set alarm" in query:
            nn = int(datetime.now().hour)
            if nn == 23:
                music_dir = "C:\\music"
                songs = os.listdir(music_dir)
                rd = random.choice(songs)
                os.startfile(os.path.join(music_dir, rd))
    # To tell joke (import pyjokes)
        elif 'tell jokes' in query:
            joke = pyjokes.get_jokes()
            speak(joke)
    # To shut down the system
        elif 'shut down the system' in query:
            os.system("shutdown /s /t 5")
    # To restart the system
        elif "restart the system" in query:
            os.system("shutdown /r /t 5")
    # To make system sleep
        elif "sleep the system" in query:
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
    # To switch the window
        elif 'switch the window' in query:
            pyautogui.keyDown('alt')
            pyautogui.press('tab')
            time.sleep(1)
            pyautogui.keyUp('alt')

        elif 'no thanks' in query:
            speak("Thank for engaging with me sweetie, have a nice day")
            sys.exit()

        speak("baby, Do you have any questions for me to ask, if so feel free to ask")









    













