import pyautogui
import os


def runstartups():
    pyautogui.sleep(2)
    os.startfile("C:/Program Files/LGHUB/lghub.exe")
    os.startfile("C:/Program Files/LGHUB/lghub_agent.exe")
    pyautogui.sleep(4)
    os.system(f"taskkill /f /im lghub.exe")
    pyautogui.sleep(2)
    os.startfile("C:/Program Files/WindowsApps/12030rocksdanister.LivelyWallpaper_1.0.137.0_x86__97hta09mmv6hy/Build/Lively.exe")
    pyautogui.sleep(2)
    os.startfile("D:/Softwares/Winstep/Nexus.exe")
    pyautogui.sleep(2)
    os.startfile("C:/Program Files/PowerToys/PowerToys.exe")
    pyautogui.sleep(2)