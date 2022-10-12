import datetime
import pyttsx3
import speech_recognition as speech
import os
import wikipedia
import webbrowser

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(talk):
    engine.say(talk)
    engine.runAndWait()


def wish():
    time_now = int(datetime.datetime.now().hour)
    if 0 <= time_now < 12:
        speak("Good Morning")
    if 12 <= time_now < 16:
        speak("Good Afternoon")
    if 16 <= time_now < 23:
        speak("Good Evening")


def listen():
    r = speech.Recognizer()
    r.energy_threshold = 1000000
    r.pause_threshold = 0.2
    r.non_speaking_duration = 0.1
    with speech.Microphone() as source:
        print("LISTENING.....")
        audio = r.listen(source)

        try:
            print("RECOGNISING...")
            order = r.recognize_google(audio)
            print(f"YOU SAID: {order}\n")

        except Exception as e:
            print(str(e))
            print("Please say that again")
            speak("Please say that again")
            return "None"
        return order


if __name__ == '__main__':
    start = True
    while start:
        ans = listen().lower()
        if "hello" in ans:
            wish()
            speak("I am Friday")
            speak("what can i do for You?")
            while True:
                query = listen().lower()
                if query == "open wikipedia":
                    os.system("start \"\" https://wikipedia.com")
                elif "wikipedia" in query:
                    speak("Searching wikipedia")
                    query = query.replace("from wikipedia", "")
                    results = wikipedia.summary(query, sentences=2)
                    speak(results)
                if query == "open youtube":
                    speak("opening youtube")
                    webbrowser.open("https://www.youtube.com", 1, True)
                elif "youtube" in query:
                    query.replace("player_1" and "in youtube", "")
                    webbrowser.open(f"https://www.youtube.com/results?search_query={query}")
                if query == "open google":
                    webbrowser.open("https://google.com")
                elif "google" in query:
                    query = query.replace("search", "")
                    query.replace("from google", "")
                    webbrowser.open(f"https://www.google.com/search?q={query}")
                if query == "shutdown":
                    os.system("shutdown /s /t 1")
                if "sleep" in query:
                    speak("Good Bye have a nice day")
                    start = False
                    break
        elif "sleep" in ans:
            break
        else:
            continue
