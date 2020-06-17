import pyttsx3
import speech_recognition as sr
import datetime
import os
import wikipedia
import random
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)


# print(voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def time():
    hour = datetime.datetime.now().hour
    minute=datetime.datetime.now().minute
    speak(hour)
    speak(minute)
def takecommands():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        audio = r.listen(source)

    try:
        print("recognising")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said:{query}")

    except Exception as e:
        print(e)
        speak("say that again please")
        query="none"
    return query


if __name__ == '__main__':

    speak("initializing")
    speak("how may i help you today")
    r=1

    while r==1:
        query=takecommands()
        if 'wikipedia'in query.lower():
            speak("searching wikipedia")
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            print(results)
            speak(results)
        elif 'hello david'in query.lower():
            speak("Hello sir")
        elif 'time'in query.lower():
            speak("right now it's")
            time()
        elif 'thank you'in query.lower():
            speak("it's my pleasure sir")
        elif 'music'in query.lower():
            speak("playing music")
            list="R://music"
            songs=os.listdir(list)


            r=random.choice(songs)
            print(r)
            os.startfile(os.path.join(list,r))




        elif 'shutdown'in query.lower():
            speak("shutting down ....")
            speak("have a nice day sir ")
            os.system("shutdown /s /t 1")
        elif 'log out'in query.lower():
            speak("logging off...")
            os.system("shutdown/l")




















