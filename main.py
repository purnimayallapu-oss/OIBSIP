##Task1:Create a basic voice assistant that can perform simple tasks based on voice
#commands. Implement features like responding to "Hello" and providing predefined responses,
#telling the time or date, and searching the web for information based on user queries.##


import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

# Start voice engine
engine = pyttsx3.init()

def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

# speech recognizer
r = sr.Recognizer()

# Welcome message
speak("Hello! I am your voice assistant.")


while True:

    # To Use microphone
    with sr.Microphone() as source:

        print("\nListening...")
        audio = r.listen(source)

    try:
        # Convert voice to text
        command = r.recognize_google(audio).lower()

        print("You said:", command)

        # Hello command
        if "hello" in command:
            speak("Hello friend")

        # Time command
        elif "time" in command:
            current_time = datetime.datetime.now().strftime("%I:%M %p")
            speak("Current time is " + current_time)

        # Exit command
        elif "exit" in command:
            speak("Goodbye")
            break
        elif "date" in command:
            current_date = datetime.datetime.now().strftime("%Y-%m-%d")
            speak("Current date is " + current_date)
        

        # if Unknown command
        else:
            speak("searching in Google")
            webbrowser.open(f"https://www.google.com/search?q={command}")

    except:
        speak("Sorry, I could not understand")