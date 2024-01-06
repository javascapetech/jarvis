import os
import pyperclip
import requests
from components.say import say

chatStr = ""


def chat(query, client):
    global chatStr
    print(chatStr)
    chatStr += f"Harshil: {query}\n Sam: "
    response = client.completions.create(
        model="text-davinci-003",
        prompt=chatStr,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    try:
        say(response.choices[0].text)
        chatStr += f"{response.choices[0].text}\n"
        return response.choices[0].text
    except Exception as e:
        print(e)
        say("I am sorry harshil but some error occurred")


def createImage(prompt, client):
    try:
        response = client.images.generate(
            model="dall-e-2",
            prompt=prompt,
            size="1024x1024",
            quality="standard",
            n=1,
        )
        image_url = response.data[0].url
        print(image_url)
        with open(f"D:/Harshil's Folder/AiImages/{prompt}.png", "wb") as f:
            f.write(requests.get(image_url).content)
        os.startfile(f"D:/Harshil's Folder/AiImages/{prompt}.png")
    except Exception as e:
        print(e)
        say("I am sorry some e error occurred! open ai sucks")


def summarize(prompt, client):
    try:
        response = client.chat.completions.create(
            model="davinci-002",
            messages=[
                {
                    "role": "system",
                    "content": "Summarize content you are provided with."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.7,
            max_tokens=64,
            top_p=1
        )
        say(response.choices[0].message.content)
        print(response.choices[0].message.content)
    except Exception as e:
        print(e)
        say("I am sorry harshil but some error occurred")


def ai(prompt, client):
    text = f"OpenAI response for Prompt: {prompt}"
    try:
        ai_response = client.completions.create(
            model="gpt-3.5-turbo",
            prompt=prompt,
            temperature=0.7,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )

        text += ai_response.choices[0].text
        pyperclip.copy(text)
        say("The output has been copied to your clipboard")
    except Exception as e:
        print(e)
        say("I am sorry sir, Some error occurred, OpenAi sucks, it must have ended daily limit")
