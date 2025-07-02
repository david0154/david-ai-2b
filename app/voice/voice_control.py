import os
import subprocess
import pyautogui
import pyttsx3

# Text-to-speech
engine = pyttsx3.init()
def speak(text):
    engine.say(text)
    engine.runAndWait()

def control_by_command(command):
    command = command.lower()
    print(f"🎯 Recognized Command: {command}")

    if "open notepad" in command:
        speak("Opening Notepad")
        os.system("start notepad")

    elif "open calculator" in command:
        speak("Opening Calculator")
        os.system("start calc")

    elif "open chrome" in command:
        speak("Opening Google Chrome")
        os.system("start chrome")

    elif "shutdown" in command:
        speak("Shutting down in 10 seconds")
        os.system("shutdown /s /t 10")

    elif "type" in command:
        text = command.split("type", 1)[1].strip()
        speak(f"Typing: {text}")
        pyautogui.write(text, interval=0.05)

    elif "hello" in command:
        speak("Hello! How can I help you?")

    else:
        speak("Sorry, I did not understand the command.")
