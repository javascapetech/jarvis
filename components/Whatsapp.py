import time
import pyautogui
import pywhatkit
from datetime import timedelta
from datetime import datetime
from components.takeCommand import takeCommand
from components.say import say


strTime = int(datetime.now().strftime("%H"))
update = int((datetime.now() + timedelta(minutes=2)).strftime("%M"))


def sendMessage():
    say("Who do you wan to message")
    a = takeCommand().lower()
    if a == 'parth':
        say("Whats the message")
        message = takeCommand()
        pywhatkit.sendwhatmsg("+917210000291", message, time_hour=strTime, time_min=update)
        time.sleep(15)
        pyautogui.press("enter")
        time.sleep(5)
        pyautogui.press("tab")
        pyautogui.press("tab")
        pyautogui.press("tab")
        pyautogui.press("tab")
        pyautogui.press("tab")
        pyautogui.press("tab")
        pyautogui.press("tab")
        pyautogui.press("tab")
        pyautogui.press("tab")
        pyautogui.press("tab")
        pyautogui.press("tab")
        pyautogui.press("tab")
        pyautogui.press("tab")
        pyautogui.press("tab")
        pyautogui.press("tab")
        pyautogui.press("tab")
        pyautogui.press("tab")
        pyautogui.press("enter")
    elif a == 'vishnu':
        say("Whats the message")
        message = takeCommand()
        pywhatkit.sendwhatmsg("+919828931999", message, time_hour=strTime, time_min=update)
        time.sleep(15)
        pyautogui.press("enter")
        time.sleep(5)
        pyautogui.press("tab")
        pyautogui.press("tab")
        pyautogui.press("tab")
        pyautogui.press("tab")
        pyautogui.press("tab")
        pyautogui.press("tab")
        pyautogui.press("tab")
        pyautogui.press("tab")
        pyautogui.press("tab")
        pyautogui.press("tab")
        pyautogui.press("tab")
        pyautogui.press("tab")
        pyautogui.press("tab")
        pyautogui.press("tab")
        pyautogui.press("tab")
        pyautogui.press("tab")
        pyautogui.press("tab")
        pyautogui.press("enter")
    elif a == "monica":
        say("Whats the message")
        message = takeCommand()
        pywhatkit.sendwhatmsg("+919784047101", message, time_hour=strTime, time_min=update)
        time.sleep(15)
        pyautogui.press("enter")
        time.sleep(5)
        pyautogui.press("tab")
        pyautogui.press("tab")
        pyautogui.press("tab")
        pyautogui.press("tab")
        pyautogui.press("tab")
        pyautogui.press("tab")
        pyautogui.press("tab")
        pyautogui.press("tab")
        pyautogui.press("tab")
        pyautogui.press("tab")
        pyautogui.press("tab")
        pyautogui.press("tab")
        pyautogui.press("tab")
        pyautogui.press("tab")
        pyautogui.press("tab")
        pyautogui.press("tab")
        pyautogui.press("tab")
        pyautogui.press("enter")
    elif a == "abhinav":
        say("Whats the message")
        message = takeCommand()
        pywhatkit.sendwhatmsg("+919799246139", message, time_hour=strTime, time_min=update)
        time.sleep(15)
        pyautogui.press("enter")
        time.sleep(5)
        pyautogui.press("tab")
        pyautogui.press("tab")
        pyautogui.press("tab")
        pyautogui.press("tab")
        pyautogui.press("tab")
        pyautogui.press("tab")
        pyautogui.press("tab")
        pyautogui.press("tab")
        pyautogui.press("tab")
        pyautogui.press("tab")
        pyautogui.press("tab")
        pyautogui.press("tab")
        pyautogui.press("tab")
        pyautogui.press("tab")
        pyautogui.press("tab")
        pyautogui.press("tab")
        pyautogui.press("tab")
        pyautogui.press("enter")
    else:
        pass
