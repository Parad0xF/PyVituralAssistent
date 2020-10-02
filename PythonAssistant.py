import pyttsx3
import speech_recognition as sr

# Function is taking commands from Microphone
# Taking commands by using Speech Recognition technologies


def take_commands():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening")

        r.pause_threshold = 0.7
        audio = r.listen(source)
    try:
        print("Recognizing")

        Query = r.recognize_google(audio, language='en-US')

        print(" the query is printed=' ", Query, "'")
    except Exception as e:
        print(e)
        print("Please say the voice command again.")
        return "None"
    return Query


def speak(audio):
    engine = pyttsx3.init()

    voices = engine.getProperty('voices')

    engine.setProperty('voices', voices[1].id)

    engine.say(audio)
    engine.runAndWait()


if __name__ == '__main__':
    while True:
        command = take_commands()

        if "exit" in command:
            speak("Exiting")
            print("Exiting")

        if "insta" in command:
            speak("Radu Enachi")
            print("@__ron__en")
