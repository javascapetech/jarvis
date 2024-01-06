import json
import os
import random
import webbrowser
from components.say import say

from dotenv import find_dotenv, load_dotenv
import base64
from requests import post, get
import json

dotenv_path = find_dotenv()
load_dotenv(dotenv_path)

CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")


def getToken():
    auth_str = CLIENT_ID + ":" + CLIENT_SECRET
    auth_bytes = auth_str.encode("utf-8")
    auth_base64 = str(base64.b64encode(auth_bytes), "utf-8")

    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization": "Basic " + auth_base64,
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {"grant_type": "client_credentials"}
    result = post(url, headers=headers, data=data)
    json_result = json.loads(result.content)
    access_token = json_result["access_token"]
    return access_token


def getAuthHeader(token):
    return {
        "Authorization": "Bearer " + token
    }


def search_for_artist(token, name):
    headers = getAuthHeader(token)
    query_url = f"https://api.spotify.com/v1/search?q={name}&type=artist&limit=1"
    result = get(query_url, headers=headers)
    json_result = json.loads(result.content)["artists"]["items"]

    if len(json_result) == 0:
        print("NO artist with this name exist")
        return None

    return json_result[0]


def search_for_songs(token, name):
    try:
        headers = getAuthHeader(token)
        query_url = f"https://api.spotify.com/v1/search?q={name}&type=track&limit=1"
        result = get(query_url, headers=headers)
        json_result = json.loads(result.content)['tracks']['items']
        return json_result
    except Exception as e:
        print(e)
        say("No songs found")


def get_song_by_artists(token, artist_id):
    query_url = f"https://api.spotify.com/v1/artists/{artist_id}/top-tracks?country=IN"
    headers = getAuthHeader(token)
    result = get(query_url, headers=headers)
    json_result = json.loads(result.content)["tracks"]
    return json_result


tkn = getToken()


def playSong(songName):
    tracks = search_for_songs(tkn, songName)
    if tracks is None:
        print("")
    else:
        for idx, song in enumerate(tracks):
            print({'name': song['name'], 'url': song['external_urls']['spotify']})
            webbrowser.open(song['external_urls']['spotify'])


def playRandomSongByArtist(artist):
    artist_info = search_for_artist(token=tkn, name=artist)
    artist_id = artist_info['id']
    tracks = get_song_by_artists(tkn, artist_id)
    songNamesWithUrls = []
    for idx, song in enumerate(tracks):
        songNamesWithUrls.append({'name': song['name'], 'url': song['external_urls']['spotify']})
    randomSong = random.choice(songNamesWithUrls)
    say(f"Playing {randomSong['name']} by {artist}")
    webbrowser.open(randomSong['url'])
