import os
import pyttsx3
import webbrowser
import subprocess

alex = pyttsx3.init('sapi5')

voices = alex.getProperty('voices')
alex.setProperty('voice', voices[0].id)

username = input("Username: ")

command = input("Your Command: ")

if command == "hello":
    alex.say("Hello, " + username)

if command == "bye":
    alex.say("Bye " + username + "See you another time.")

if command == "open youtube":
    alex.say("Opening YouTube")
    webbrowser.open_new_tab("youtube.com")

if command == "open stackoverflow":
    alex.say("Opening Stackoverflow")
    webbrowser.open_new_tab("https://stackoverflow.com/")

if command == "open my website":
    alex.say("Opening Your Website")
    webbrowser.open_new_tab("ahmed-alfadhel.w3spaces.com")

if command == "who am i":
    alex.say("You are " + username)

if command == "who is my brother":
    alex.say("You're brother is Hasan")

if command == "who are you":
    alex.say("I'm Alex you're personal assistant and I was made by you.")

if command == "open github":
    alex.say("Opening Github")
    webbrowser.open_new_tab("github.com")

if command == "open desktop":
    alex.say("Opening Desktop")
    subprocess.Popen('explorer "C:/Users/ahmed/Desktop"')

if command == "open downloads":
    alex.say("Opening Downloads")
    subprocess.Popen('explorer "C:/Users/ahmed/Downloads"')

if command == "open documents":
    alex.say("Opening Documents")
    subprocess.Popen('explorer "C:/Users/ahmed/Documents"')

if command == "open pirctures":
    alex.say("Opening Pictures")
    subprocess.Popen('explorer "C:/Users/ahmed/Pictures"')

if command == "open music":
    alex.say("Opening Music")
    subprocess.Popen('explorer "C:/Users/ahmed/Music"')

if command == "open videos":
    alex.say("Opening Videos")
    subprocess.Popen('explorer "C:/Users/ahmed/Videos"')

if command == "open google":
    alex.say("Redirecting You To Google!")
    webbrowser.open_new_tab("google.com")

if command == "code":
    alex.say("Opening Visual Studio Code...")
    os.startfile("C:\\Users\\ahmed\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")

if command == "chrome":
    alex.say("Opening Google Chrome...")
    os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")

if command == "play lofi":
    alex.say("Playing Lofi Hip Hop")
    os.startfile("C:\\Users\\ahmed\\Desktop\\lofi1.mp3")

alex.runAndWait()