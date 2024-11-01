import cmd
import requests
import os
from auth import authenticate, read_token

class SpotifyCLI(cmd.Cmd):
    prompt = ">> "
    intro = "Welcome to Scotty's Spotify CLI"

    def __init__(self):
        super().__init__()

    # ---------Initialization & Cleanup---------
    def preloop(self):
        authenticate()

    def postloop(self):
        os.remove("token.txt")

    def precmd(self, line):
        return line

    def postcmd(self, stop, line):
        print()
        return stop

    def do_hello(self, line):
        """Say hi"""
        print("Hello world")

    def do_quit(self, line):
        """Close Spotify CLI"""
        print("Exiting Scotty's Spotify CLI")
        return True

    # ----------------Spotify APIs--------------
    def do_search(self, text):
        """Search spotify for Miles Davis"""
        token = read_token()
        url = "https://api.spotify.com/v1/search"

        headers = {"Authorization": f"Bearer {token}", "accept": "application/json",}
        res = requests.get(url, headers=headers, params={
            "type": "album",
            "q": {
                "artist": "Miles Davis"
            },
            "limit": 5
        }).json()
        print(res.get("albums").get("items"))
        print(f"you typed {text}")
        # print(res.json())

