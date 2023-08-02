import pyttsx3
import speech_recognition as sr
import pyaudio
import datetime
import webbrowser
import pyjokes
import randfacts
import os
import psutil
import wikipedia
import pyautogui
import requests
import json
from wikisel import *
from selyt import *


engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
repeat=0
screenshotrepeat=0
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold=0.8
        audio=r.listen(source)

        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-in")

        except Exception as e:
            print("I am sorry,please repeat it")
            speak("I am sorry,please repeat it,Sir")
            return "None"
        return query

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Hello Good Morning")
        print("Good Morning")
    elif hour>=12 and hour<18:
        speak("hello Good Afternoon")
        print("Good Afternoon")
    else:
        speak("Good Evening ")
        print("Good Evening")




if __name__ == '__main__':
    wishMe()
    speak("how can I help you , dude")
    print("how can I help you , dude")
    while True:
        text = takecommand().lower()

        if "tell" and "me" and "about" in text and "yourself" in text:
           speak("I am bro"
               "I am your personal assistant "
                 "I am usefull fro music lovers ,book lovers,bodcast listeners"
                 "if you want to know about news simply ask, "
                 "bro, tell me todays NEWS ")
           print("I am good,what can i do for you!")
        elif "hello" and"Hai" in text:
            speak("hello bro")
            print("Hello bro")
        elif "play" and "song" and "from" and "youtube" in text:
            speak("Playing songs from youtube")
            print("Playing songs from youtube")
            webbrowser.open(url="https://www.youtube.com/results?search_query=songs")
        elif "open" and "instagram" in text:
            speak("opening your instagram page, Sir")
            print("opening your instagram page")
            webbrowser.open(url="https://www.instagram.com/")
        elif 'date' in text:
            curDate = datetime.datetime.now().strftime("%d:%B:%Y")
            curDay = datetime.datetime.now().strftime("%A")
            print(f"Today's date is {curDate} and the day {curDay}")
            speak(f"Today's date is {curDate} and the day {curDay}")
        elif 'time' in text:
            curTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"Now the Time is {curTime} ")
            speak(f"Now the Time is {curTime} ")
        elif "open my browser" in text:
            speak("Opening your Browser")
            webbrowser.open(url="https://duckduckgo.com")
        elif 'open' and 'linkedin' in text:
            speak('Opening LinkedIn in Webrowser')
            webbrowser.open(url="https://linkedin.com")
        elif 'open' and 'K S R I E T' and 'College' and 'website' in text:
            speak('Opening K S R I E T college of Technology in Webrowser')
            webbrowser.open(url="https://www.ksriet.ac.in")
        elif "open" in text and "Github":
            speak("Opening github in your Browser")
            webbrowser.open(url="https://github.com")
        elif "open" in text and "Youtube":
            speak("Opening youtube in your Browser")
            webbrowser.open(url="https://youtube.com")


        elif"joke" in text:
            Joke = pyjokes.get_joke('en','neutral')
            print(Joke)
            speak(Joke)

        elif "facts" in text:
            Fact = randfacts.get_fact()
            print(Fact)
            speak(Fact)


        elif "Battery" and "percentage" in text:
            usage = str(psutil.cpu_percent())
            speak('cpi is at' + usage)

            battery = psutil.sensors_battery()
            speak("battery is at")
            speak(battery.percent)


        elif "according to wikipedia" in text:
            speak("searcing in wikipedia...")
            word = text.replace("wikipedia", "")
            results = wikipedia.summary(word, sentences=2)
            speak("according to wikipedia")
            print(results)
            speak(results)

        elif "search" and "in" and "google" in text:
            speak("What Should I search ,Sir")
            googlequery = takecommand()
            webbrowser.open(url=f"https://www.google.com/search?q={googlequery}")
            speak("Opening Google Chrome for your search result")

        elif "take" in text and "screenshot" in text:
            img = pyautogui.screenshot()
            img.save(f"D:\\Logesh T R\\AI-Voice-Assistant-main\\screenshot\\img{screenshotrepeat}.png")
            screenshotrepeat+=1
            speak("Done sir,I am saving it.")


        elif "take" and "notes" in text:
            speak("what should i write sir?")
            notes = takecommand()
            repeat += 1
            file = open(f"D:\\Logesh T R\\AI-Voice-Assistant-main\\Notes\\notes{repeat}.txt",'w')
            speak("should i include date and time ?")
            if "yes" or "sure" in text:
                curTime = datetime.datetime.now().strftime("%H:%M:%S")
                curDate = datetime.datetime.now().strftime("%d:%B:%Y")
                file.write(curTime)
                file.write(curDate)
                file.write(':-')
                file.write(notes)
                speak("Done taking notes sir")

            else:
                file.write(notes)
                speak("Done taking notes sir")

        elif "show" and "notes" in text:
            speak("opening notes")
            file = open(f'notes{repeat}.txt','r')#formating text/string
            print(file.read())
            speak(file.read())

        elif "news" in text:
            api_address =  "https://newsapi.org/v2/top-headlines?country=in&apiKey=3c5b2cc319c74916990c5ad5923054ab"

            response = requests.get(api_address)
            news_json = json.loads(response.text)

            count = 3

            print("Here are today's Top headlines")
            speak("Here are today's Top headlines")
            for news in news_json['articles']:
                if count>0:
                    T = str(news['title'])
                    print(T)
                    speak(T)
                    count -= 1

        elif "information" in text:
            speak("please name the topic")
            topic = takecommand()
            print("Searching {} in wikipedia".format(topic))
            speak("Searching {} in wikipedia".format(topic))
            assist = info()
            assist.getinfo(topic)
        elif "play" in text and "online" in text:
            speak("what do you want me to play")
            title = takecommand()
            print("Playing {} in youtube".format(title))
            speak("Playing {} in youtube".format(title))
            bot = music()
            bot.play(title)
        elif "go offline" in text:
            speak("Iam going offline Bye bye")
            print("Going Offline...😀")
            quit()



