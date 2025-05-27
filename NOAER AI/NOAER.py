import datetime
from email import message
import webbrowser
from numpy import tile 
import pyttsx3
import speech_recognition
import requests
from bs4 import BeautifulSoup
import os
import pyautogui
import random
import speedtest
import cv2
import time
import numpy as np
import sys
import mediapipe as mp
import pywhatkit as kit
import operator
import wikipedia
########################for pass security#########################################
for i in range(3):
    a = input("Enter Password to open Jarvis :- ")
    pw_file = open("password.txt","r")
    pw = pw_file.read()
    pw_file.close()
    if (a==pw):
        print("WELCOME SIR ! PLZ SPEAK [WAKE UP] TO LOAD ME UP")
        break
    elif (i==2 and a!=pw):
        exit()

    elif (a!=pw):
        print("Try Again")
#####################################################################################
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
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

def alarm(query):
    timehere = open("Alarmtext.txt","a")
    timehere.write(query)
    timehere.close()
    os.startfile("alarm.py")


if __name__ == "__main__":
    while True:
        query = takeCommand().lower()
        if "wake up" in query:
            from GreetMe import greetMe
            greetMe()

            while True:
                query = takeCommand().lower()
                if "go to sleep" in query:
                    speak("Ok sir , You can call me anytime")
                    break 

                #################### JARVIS: THe Trilogy 2.0 #####################

                elif "change password" in query:
                    speak("What's the new password")
                    new_pw = input("Enter the new password\n")
                    new_password = open("password.txt","w")
                    new_password.write(new_pw)
                    new_password.close()
                    speak("Done sir")
                    speak(f"Your new password is{new_pw}")

                elif "schedule my day" in query:
                    tasks = [] #Empty list 
                    speak("Do you want to clear old tasks (Plz speak YES or NO)")
                    query = takeCommand().lower()
                    if "yes" in query:
                        file = open("tasks.txt","w")
                        file.write(f"")
                        file.close()
                        no_tasks = int(input("Enter the no. of tasks :- "))
                        i = 0
                        for i in range(no_tasks):
                            tasks.append(input("Enter the task :- "))
                            file = open("tasks.txt","a")
                            file.write(f"{i}. {tasks[i]}\n")
                            file.close()
                    elif "no" in query:
                        i = 0
                        no_tasks = int(input("Enter the no. of tasks :- "))
                        for i in range(no_tasks):
                            tasks.append(input("Enter the task :- "))
                            file = open("tasks.txt","a")
                            file.write(f"{i}. {tasks[i]}\n")
                            file.close()


                elif "focus mode" in query:
                    a = int(input("Are you sure that you want to enter focus mode :- [1 for YES / 2 for NO "))
                    if (a==1):
                        speak("Entering the focus mode....")
                        os.startfile("D:\\Coding\\Youtube\\Jarvis\\FocusMode.py")
                        exit()

                    
                    else:
                        pass


                elif "search" in query:   #EASY METHOD
                    query = query.replace("search","")
                    query = query.replace("NOAER","")
                    pyautogui.press("super")
                    pyautogui.typewrite(query)
                    pyautogui.sleep(2)
                    pyautogui.press("enter")                       
                     
                elif "internet speed" in query:
                    wifi  = speedtest.Speedtest()
                    upload_net = wifi.upload()/1048576         #Megabyte = 1024*1024 Bytes
                    download_net = wifi.download()/1048576
                    print("Wifi Upload Speed is", upload_net)
                    print("Wifi download speed is ",download_net)
                    speak(f"Wifi download speed is {download_net}")
                    speak(f"Wifi Upload speed is {upload_net}")
                
                
        
                elif "screenshot" in query:
                     import pyautogui #pip install pyautogui
                     im = pyautogui.screenshot()
                     im.save("ss.jpg")

                elif "click my photo" in query:
                    pyautogui.press("super")
                    pyautogui.typewrite("camera")
                    pyautogui.press("enter")
                    pyautogui.sleep(2)
                    speak("SMILE")
                    pyautogui.press("enter")

                
                

                ############################################################
                elif "hello" in query:
                    speak("Hello sir, how are you ?")
                elif "i am fine" in query:
                    speak("that's great, sir")
                elif "how are you" in query:
                    speak("Perfect, sir")
                elif "thank you" in query:
                    speak("you are welcome, sir")
                
                elif "tired" in query:
                    speak("Playing your favourite songs, sir")
                    a = (1,2,3)
                    b = random.choice(a)
                    if b==1:
                        webbrowser.open("https://www.youtube.com/watch?v=iKq8uzfwK8Y&t=31s")
                    

                elif "pause" in query:
                    pyautogui.press("k")
                    speak("video paused")
                elif "play" in query:
                    pyautogui.press("k")
                    speak("video played")
                elif "mute" in query:
                    pyautogui.press("m")
                    speak("video muted")
                elif "next" in query:
                    pyautogui.press("shift+N")
                    speak("next video played")

                elif "google" in query:
                    from SearchNow import searchGoogle
                    searchGoogle(query)


                elif "youtube" in query:
                    from SearchNow import searchYoutube
                    searchYoutube(query)


                elif "wikipedia" in query:
                    from SearchNow import searchWikipedia
                    searchWikipedia(query)

                
            


                

                elif "temperature" in query:
                    search = "temperature in delhi"
                    url = f"https://www.google.com/search?q={search}"
                    r  = requests.get(url)
                    data = BeautifulSoup(r.text,"html.parser")
                    temp = data.find("div", class_ = "BNeawe").text
                    speak(f"current{search} is {temp}")
                elif "weather" in query:
                    search = "temperature in delhi"
                    url = f"https://www.google.com/search?q={search}"
                    r  = requests.get(url)
                    data = BeautifulSoup(r.text,"html.parser")
                    temp = data.find("div", class_ = "BNeawe").text
                    speak(f"current{search} is {temp}")

                elif "set an alarm" in query:
                    print("input time example:- 10 and 10 and 10")
                    speak("Set the time")
                    a = input("Please tell the time :- ")
                    alarm(a)
                    speak("Done,sir")
                           
                elif "the time" in query:
                    strTime = datetime.datetime.now().strftime("%H:%M")    
                    speak(f"Sir, the time is {strTime}")
                elif "finally sleep" in query:
                    speak("Going to sleep,sir")
                    exit()

                elif "remember that" in query:
                    rememberMessage = query.replace("remember that","")
                    rememberMessage = query.replace("jarvis","")
                    speak("You told me to remember that"+rememberMessage)
                    remember = open("Remember.txt","a")
                    remember.write(rememberMessage)
                    remember.close()
                elif "what do you remember" in query:
                    remember = open("Remember.txt","r")
                    speak("You told me to remember that" + remember.read())

                elif "shutdown system" in query:
                    speak("Are You sure you want to shutdown")
                    shutdown = input("Do you wish to shutdown your computer? (yes/no)")
                    if shutdown == "yes":
                        os.system("shutdown /s /t 1")

                    elif shutdown == "no":
                        break
########################################## NOAER 2 #############################################################################################
                elif 'youtube' in query:
                   speak("what you will like to watch ?")
                   qrry = takeCommand().lower()
                   query = query.replace("open","")
                   kit.playonyt(f"{qrry}")
                
                elif 'search on youtube' in query:
                    query = query.replace("search on youtube", "")
                    webbrowser.open(f"www.youtube.com/results?search_query={query}")

                elif 'close youtube' in query:
                    os.system("taskkill /f /im msedge.exe")
                
                elif 'open google' in query:
                    speak("what should I search ?")
                    qry = takeCommand().lower()
                    webbrowser.open(f"{qry}")
                    results = wikipedia.summary(qry, sentences=2)
                    speak(results)
                
                elif 'close google' in query:
                    os.system("taskkill /f /im msedge.exe")

                elif 'close vlc' in query:
                    os.system("taskkill /f /im vlc.exe")
                
                elif "restart the system" in query:
                    speak("Are You sure you want to restart")
                    restart = input("Do you wish to restart your computer? (yes/no)")
                    if restart == "yes":
                        os.system("shutdown /r /t 5")
                
                    elif restart == "no":
                        break

                elif "Lock the system" in query:
                    os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

                elif "open notepad" in query:
                    npath = "C:\WINDOWS\system32\\notepad.exe"
                    os.startfile(npath)

                elif "close notepad" in query:
                    os.system("taskkill /f /im notepad.exe")    

                elif "open command prompt" in query:
                    os.system("start cmd")

                elif "close command prompt" in query:
                    os.system("taskkill /f /im cmd.exe")

                elif "start camera" in query:
                    cap = cv2.VideoCapture(0)
                    while True:
                        ret, img = cap.read()
                        cv2.imshow('webcam', img)
                        k = cv2.waitKey(50)
                        if k==27:
                            break;
                    cap.release()
                    cv2.destroyAllWnd
                
                elif "volume up" in query:
                    pyautogui.press("volumeup")
                    pyautogui.press("volumeup")
                    pyautogui.press("volumeup")

                elif "volume down" in query:
                    pyautogui.press("volumedown")
                    pyautogui.press("volumedown")
                    pyautogui.press("volumedown")

                elif "mute" in query:
                    pyautogui.press("volumemute")

                elif "refresh" in query:
                    pyautogui.moveTo(1551,551, 2)
                    pyautogui.click(x=1551, y=551, clicks=1, interval=0, button='right')
                    pyautogui.moveTo(1620,667, 1)
                    pyautogui.click(x=1620, y=667, clicks=1, interval=0, button='left')

                elif "scroll down" in query:
                    pyautogui.scroll(1000)

                elif "rectangular" in query:
                    pyautogui.hotkey('win')
                    time.sleep(1)
                    pyautogui.write('paint')
                    time.sleep(1)
                    pyautogui.press('enter')
                    pyautogui.moveTo(100, 193, 1)
                    pyautogui.rightClick
                    pyautogui.click()
                    distance = 300
                    while distance > 0:
                        pyautogui.dragRel(distance, 0, 0.1, button="left")
                        distance = distance - 10
                        pyautogui.dragRel(0, distance, 0.1, button="left")
                        pyautogui.dragRel(-distance, 0, 0.1, button="left")
                        distance = distance - 10
                        pyautogui.dragRel(0, -distance, 0.1,)

                elif "take screenshot" in query:
                    speak('tell me a name for the file')
                    name = takeCommand().lower()
                    time.sleep(3)
                    img = pyautogui.screenshot()
                    img.save(f"{name}.png")
                    speak("screenshot saved")

                elif "close paint" in query:
                    os.system("taskkill /f /im mspaint.exe")

                elif "who are you" in query:
                    print('My Name Is Six')
                    speak('My Name Is Six')
                    print('I can Do Everything that my creator programmed me to do')
                    speak('I can Do Everything  that my creator programmed me to do')

                elif "who created you" in query:
                    print('I Do not Know His Name, I created with Python Language, inVisual Studio Code.')
                    speak('I Do not Know His Name, I created with Python Language, inVisual Studio Code.')

                elif "open notepad and write my channel name" in query:
                    pyautogui.hotkey('win')
                    time.sleep(1)
                    pyautogui.write('notepad')
                    time.sleep(1)
                    pyautogui.press('enter')
                    time.sleep(1)
                    pyautogui.write("REAL Boss", interval = 0.1)

                elif 'type' in query: #10
                    query = query.replace("type", "")
                    pyautogui.write(f"{query}")

                if 'open chrome' in query:
                   os.startfile('C:\Program Files\Google\Chrome\Application\chrome.exe')

                elif 'maximize this window' in query:
                    pyautogui.hotkey('alt', 'space')
                    time.sleep(1)
                    pyautogui.press('x')
         
                elif 'google search' in query:
                    query = query.replace("google search", "")
                    pyautogui.hotkey('alt', 'd')
                    pyautogui.write(f"{query}", 0.1)
                    pyautogui.press('enter')

                elif 'youtube search' in query:
                    query = query.replace("youtube search", "")
                    pyautogui.hotkey('alt', 'd')
                    time.sleep(1)
                    pyautogui.press('tab')
                    pyautogui.press('tab')
                    pyautogui.press('tab')
                    pyautogui.press('tab')
                    time.sleep(1)
                    pyautogui.write(f"{query}", 0.1)
                    pyautogui.press('enter')

                elif 'open new window' in query:
                    pyautogui.hotkey('ctrl', 'n')

                elif 'open incognito window' in query:
                    pyautogui.hotkey('ctrl', 'shift', 'n')

                elif 'open history' in query:
                    pyautogui.hotkey('ctrl', 'h')

                elif 'open downloads' in query:
                    pyautogui.hotkey('ctrl', 'j')

                elif 'previous tab' in query:
                    pyautogui.hotkey('ctrl', 'shift', 'tab')

                elif 'next tab' in query:
                    pyautogui.hotkey('ctrl', 'tab')

                elif 'close tab' in query:
                    pyautogui.hotkey('ctrl', 'w')
                
                elif 'close window' in query:
                    pyautogui.hotkey('ctrl', 'shift', 'w')

                elif 'clear browsing history' in query:
                    pyautogui.hotkey('ctrl', 'shift', 'delete')

                elif 'close chrome' in query:
                    os.system("taskkill /f /im chrome.exe")



