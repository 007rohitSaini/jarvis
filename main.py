# dependencies
import pyttsx3
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
