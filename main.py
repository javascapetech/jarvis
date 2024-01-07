from components.clap import MainClap
from components.takeCommand import takeCommand
from components.say import say

if __name__ == '__main__':
    while True:
        print("listening...")
        isClapped = MainClap()
        if isClapped:
            say("sam at your service sir!")
            while True:
                print("listening")
                query = takeCommand()
