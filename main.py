import speech_recognition as sr
import os
from gtts import gTTS
import datetime
import pyttsx3
import playsound
import warnings
import pyaudio
import random
import datetime
import time
import calendar
import wikipedia

warnings.filterwarnings("ignore")

engine = pyttsx3.init()
voices = engine.getProperty('rate')
engine.setProperty('rate', 175)


def talk(audio):  # storing audio
    engine.say(audio)
    engine.runAndWait()


def get_voice_command():  # recoding the audio with the help of google
    record = sr.Recognizer()

    with sr.Microphone() as source:
        record.adjust_for_ambient_noise(source)
        print("Listening...")
        audio = record.listen(source, timeout=10)

    data = ''

    try:
        data = record.recognize_google(audio)
    except sr.UnknownValueError:
        engine.say("Assistant could not understand the audio")
    except sr.RequestError as ex:
        engine.say("Request Error from Google Speech Recognition" + ex)
    return data


def response(text):  # Air responding to the usr
    tts = gTTS(text=text, lang="en")
    audio = "Audio.mp3"
    tts.save(audio)
    playsound.playsound(audio)
    os.remove(audio)  # removing audio as a nessesity to keep it clear


def call(text):  # calling air
    action_call = "air"
    text = text.lower()
    if action_call in text:
        return True
    return False


def today_date():
    now = datetime.datetime.now()
    date_now = datetime.datetime.today()
    week_now = calendar.day_name[date_now.weekday()]
    month_now = now.month
    day_now = now.day

    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
    ]

    ordinals = [
        "1st",
        "2nd",
        "3rd",
        "4th",
        "5th",
        "6th",
        "7th",
        "8th",
        "9th",
        "10th",
        "11th",
        "12th",
        "13th",
        "14th",
        "15th",
        "16th",
        "17th",
        "18th",
        "19th",
        "20th",
        "21st",
        "22nd",
        "23rd",
        "24th",
        "25th",
        "26th",
        "27th",
        "28th",
        "29th",
        "30th",
        "31st",
    ]

    return "Today is " + week_now + ", " + months[month_now - 1] + " the " + ordinals[day_now - 1]


def wiki_finder(text):
    extras = ["wikipedia", "who", "is", "search", "on", "at", " "]
    original_text = text.split()
    to_be_searched = ""
    for imp in range(0, len(original_text)):
        if original_text[imp] != ".":
            if original_text[imp] not in extras:
                to_be_searched = to_be_searched + original_text[imp]
                to_be_searched = to_be_searched + " "
        else:
            break
    return to_be_searched


while True:
    try:
        text = get_voice_command()
        speak = ""

        if "date" in text or "day" in text or "month" in text or "what do you think today's date is" in text:
            get_today = today_date()
            speak = speak + " " + get_today

        elif "time" in text:
            now = datetime.datetime.now()
            meridiem = ""
            if now.hour >= 12:
                meridiem = "pm"
                hour = now.hour - 12
            else:
                meridiem = "am"
                hour = now.hour

            if now.minute < 10:
                minute = "0" + str(now.minute)
            else:
                minute = str(now.minute)
            speak = speak + " " + "It is " + str(hour) + ":" + minute + " " + meridiem + " ."

        elif "wikipedia" in text or "Wikipedia" in text:
            object = wiki_finder(text)
            wiki = wikipedia.summary(object, sentences=2)
            speak = speak + " " + wiki
            wiki = ""

        elif "thank you" in text or "shutdown" in text:
            talk("see you again")
            break

        response(speak)
        print(speak)
    except:
        talk("I didn't understand what you said please try again")
