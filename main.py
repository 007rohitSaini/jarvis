# dependencies
import pyttsx3  # pip install pyttsx3
import time
import speech_recognition as sr  # pip install speechRecognition
import datetime
import wikipedia  # pip install wikipedia
import webbrowser
import os
import smtplib
import selenium
import wolframalpha
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import requests
from nasa import api

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=clientid,
                                                           client_secret=))
app_id = "EJTJ3V-H2HUVHK2KQ"

# Instance of wolf ram alpha
# client class
client = wolframalpha.Client(app_id)

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning!")

    elif 12 <= hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    #codePath = "C:\\Users\\HP\\PycharmProject\\opencv\\main.py"
    #      b     os.startfile(codePath)
    speak("I am up sir . Please tell me how may I help you")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)
        print("Say that again please...")
        return "None"
    return query


def NewsFromBBC():
    # BBC news api
    main_url = " https://newsapi.org/v1/articles?source=bbc-news&sortBy=top&apiKey=9f5fc10518c34062a11072520b627072"

    # fetching data in json format
    open_bbc_page = requests.get(main_url).json()

    # getting all articles in a string article
    article = open_bbc_page["articles"]

    results = []

    for ar in article:
        results.append(ar["title"])

    for i in range(len(results)):
        # printing all trending news
        print(i + 1, results[i])
    return results



if __name__ == "__main__":
    wishMe()
    while True:
        try:
    # if 1:
            query = takeCommand().lower()

            # Logic for executing tasks based on query
            if 'wikipedia' in query:
                speak('Searching Wikipedia...')
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                print(results)
                speak(results)

            elif 'space' in query:
                if 'who is in Space' in query:
                    speak(api.issMember()) 
                elif 'weather on mars' in query:
                    speak(api.marsweather)       

            elif 'open youtube' in query:
                webbrowser.open("youtube.com")

            elif 'open google' in query:
                webbrowser.open("google.com")

            elif 'open stackoverflow' in query:
                webbrowser.open("stackoverflow.com")

            elif 'play music' in query:
                music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
                songs = os.listdir(music_dir)
                print(songs)
                os.startfile(os.path.join(music_dir, songs[0]))

            elif 'the time' in query:
                strTime = datetime.datetime.now().strftime("%H")
                strmin = datetime.datetime.now().strftime("%M")
                strsec = datetime.datetime.now().strftime("%S")

                speak(f"Sir, the time is {strTime} hours, {strmin} minutes and {strsec} seconds")

            elif 'open code' in query:
                codePath = "C:\\Users\\HP\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                os.startfile(codePath)

            elif 'temperature' in query:
                res = client.query(query)
                answer = next(res.results).text
                speak(answer)

            elif 'news' in query:
                # BBC news api
                main_url = " https://newsapi.org/v1/articles?source=bbc-news&sortBy=top&apiKey=9f5fc10518c34062a11072520b627072"

                # fetching data in json format
                open_bbc_page = requests.get(main_url).json()

                # getting all articles in a string article
                article = open_bbc_page["articles"]

                # empty list which will
                # contain all trending news
                results = []

                for ar in article:
                    results.append(ar["title"])

                for i in range(len(results)):
                    # printing all trending news
                    print(i + 1, results[i])
                speak(results)

            elif 'location' in query:
            
                res = requests.get("https://ipinfo.io/")
                data = res.json()

                print(data)

                base = "https://maps.googleapis.com/maps/api/geocode/json?latlng="
                key = "&key=AIzaSyD8cmQUtPd68HL_X1IodN3cl7ll3posbls"
                loc = data['loc']
                url = f"{base}{loc}{key}"
                print(url)
            elif "bye" in query:
                exit()

            elif "email" in query:
                try:
                    speak("To whom you want to send email")
                    email = takeCommand()
                    confirm = email.replace(" ", '')
                    speak("please confirm email")
                    speak(confirm)
                    print(confirm)
                    ok = takeCommand()
                    while ok == "yes" or "ok" or "okay":
                        to = confirm
                    else:
                        to = input("please enter email manually.")
                        speak("please Enter email manually.")

                    time.sleep(5)
                    speak("Okay . what should i say.")
                    content = takeCommand()
                    speak("Email has been sent!")
                except Exception as e:
                    print(e)
                    speak("i am getting some error .please try again after some time.")
                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.ehlo()
                server.starttls()
                server.login('rohitsaini1427@gmail.com', 'saini@123')
                server.sendmail('rohitsaini1427@gmail.com', to, content)
                server.close()
        except:      
            if "what" or "Who" or "Which" or "how" in query:
                res = client.query(query)
                answer = next(res.results).text
                print(answer)
                speak(answer)
        
"""import pyttsx3
import os
import calender
import speech_recognition as sr

# initiate speech to text
# use sapi5 for windows , nsss for MAC OS x . espeak is on linux (avoid using espeak)
# get os name form platform
engine = pyttsx3.init(driverName='sapi5')
# Set voice to male (change to 1 to get female voice) and volume to 1(1 is max and 0 is min)
voices = engine.getProperty('voices')
volume = engine.getProperty('volume')
engine.setProperty('voice', voices[0].id)
engine.setProperty('volume', 1.0)


class speak_tts:
    def __init__(self, speech, action):
        self.speech = speech
        self.action = action

    def speak(self):
        engine.say(self.speech)
        engine.runAndWait()
        engine.stop()

    def action(self):
        stream = os.popen(self.action)
        return stream.read()


class speech_reacognition:
    pass


class main:
    def __init__(self, speech):
        self.speech = speech

    def boot(self):
        pass


if __name__ == '__main__':

    while True:
        text = input("What you want to speak")
        speak = speak_tts(text, 0)
        speak.speak()

    res = calender.get_event_data()
    print(res)
"""
