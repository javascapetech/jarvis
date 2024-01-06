import os
import pyautogui
import webbrowser
import datetime
import random
from dotenv import find_dotenv, load_dotenv
from openai import OpenAI
from components.clap import MainClap
from components.computerVision import handDetectionFunc, handWithCursor, shutDownConfirmer, objectDetector
from components.openai import chat, createImage, summarize, ai
from components.takeCommand import takeCommand
from components.runStartups import runstartups
from components.Whatsapp import sendMessage
from components.say import say
from components.Spotify import playRandomSongByArtist, playSong

dotenv_path = find_dotenv()
load_dotenv(dotenv_path)
API_KEY = os.getenv("API_KEY")

client = OpenAI(
    api_key=API_KEY
)

dictapp = {"commandprompt": "cmd", "paint": "paint", "word": "winword", "excel": "cexcel", "chrome": "chrome",
           "vs code": "code", "powerpoint": "powerpnt", "pycharm": 'pycharm', "whatsapp": "whatsapp",
           "microsoft store": "WinStore.App", "edge": "msedge", "spotify": "spotify"}

if __name__ == '__main__':
    # runstartups()
    while True:
        print("listening...")
        isClapped = MainClap()
        if isClapped:
            say("sam at your service sir!")
            while True:
                print("listening")
                query = takeCommand()
                sites = [["youtube", "https://youtube.com"], ["leetcode", "https://leetcode.com/problemset/"],
                         ["instagram", "https://instagram.com/"], ["any watch", "https://aniwatch.to/"],
                         ["github", "https://github.io/"], ["wikipedia", "https://www.wikipedia.com"],
                         ["amazon", "https://www.amazon.in/"], ["javascript", "https://javascapetechnologies.web.app"],
                         ["kids are kids" "https://kidzrkidz-jodhpur.web.app"]]
                for site in sites:
                    if f"open {site[0]}".lower() in query.lower():
                        say(f"Okay! lets open {site[0]}")
                        webbrowser.open((site[1]))
                if "close" in query.lower():
                    keys = list(dictapp.keys())
                    for app in keys:
                        if app in query.lower():
                            os.system(f"taskkill /f /im {dictapp[app]}.exe")
                elif "play" and "song" in query.lower():
                    say("Sure i will play some music")
                    playRandomSongByArtist("Eminem")
                    say("Anything else you want me to help with")
                elif "play" in query.lower():
                    say(f"Sure i will play some {query.lower().replace('play ', '')}")
                    playSong(query.lower().replace('play ', ''))
                    say("Anything else you want me to help with")
                elif "search in youtube" in query.lower():
                    webbrowser.open(
                        f"https://www.youtube.com/results?search_query={query.lower().replace('search ', '').replace('in ', '').replace('youtube ', '')}")
                elif "open" in query.lower().replace(" ", ""):
                    query = query.replace("open", "")
                    query = query.replace("sam", "")
                    pyautogui.press("super")
                    pyautogui.typewrite(query)
                    # pyautogui.sleep(2)
                    pyautogui.press("enter")
                    pass
                elif "the time" in query.lower():
                    time = datetime.datetime.now().strftime("%H:%M")
                    say(f"Sir the time is {time}")
                elif "go to sleep" in query.lower():
                    say("Bye Bye! Take Care")
                    break
                elif "shutdown computer" in query.lower():
                    say("are you sure")
                    res = shutDownConfirmer()
                    if res:
                        say("Ok sir I am Shutting Your Computer Down in 5 Seconds")
                        os.system('shutdown /s /t 5')
                    else:
                        say("Ok sir i will not shutdown your computer")
                elif "restart computer" in query.lower():
                    say("Ok sir I am restarting your pc")
                    os.system('shutdown /r /t 5')
                elif "create" and "image" in query.lower():
                    pro = query.lower().replace("create", "").replace("image", "").replace("of", "").replace("sam",
                                                                                                             "")
                    say(f"Ok sir I am creating an image of {pro}")
                    createImage(pro, client)
                elif "create" and "website" in query.lower():
                    print("creating a simple website...")
                    ai(query.lower().replace("hey", "").replace("sam", ""), client)
                elif "use whatsapp" in query.lower():
                    sendMessage()
                elif "summarise".lower() in query.lower():
                    print("summarising...")
                    summarize(query.lower().replace("summarise", ""), client)
                elif "control" and "volume" in query.lower():
                    handDetectionFunc()
                elif "control" and "mouse" in query.lower():
                    handWithCursor()
                elif "set" and "alarm" in query.lower():
                    while True:
                        print("Listening...")
                        say("What time do you want alarm to be: ")
                        tt = takeCommand().upper().replace(".", "")
                        try:
                            alarmTime = datetime.datetime.now().strptime(tt, "%I:%M %p")
                            print("Alarm has been set up")
                            while True:
                                currentTime = datetime.datetime.now()
                                if alarmTime.hour == currentTime.hour and alarmTime.minute == currentTime.minute:
                                    say("Wake Up")
                                    say("Wake Up")
                                    say("Wake Up")
                                    os.startfile("D:/Harshil's Folder/songs/slimshady.mp3")
                                    break
                            break
                        except Exception as e:
                            print(e)
                            say("can you please repeat sir")
                elif "object" and "detection" in query.lower():
                    objectDetector()
                elif "Using ai".lower() in query.lower():
                    ai(query, client)
                elif "screenshot" in query.lower():
                    im = pyautogui.screenshot()
                    randomInd = random.randint(0, 1000000)
                    im.save(f"D:/Harshil's Folder/ss/ss{randomInd}.jpg")
                elif query == 'None':
                    print("")
                elif "Search".lower() in query.lower():
                    webbrowser.open(f"https://www.google.com/search?q={query.lower().replace('search', '')}")
                else:
                    print("Chatting...")
                    chat(query, client)
