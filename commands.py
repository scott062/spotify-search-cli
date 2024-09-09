import requests
from auth import read_token

def search():
    token = read_token()
    url = "https://api.spotify.com/v1/search"

    headers = {"Authorization": f"Bearer {token}", "accept": "application/json",}
    res = requests.get(url, headers=headers, params={"type": "album", "q": {"artist": "Miles Davis"}})
    print(res.json())


def pause():
    print("pausing")
    pass

def go_next():
    print("going next")
    pass

def go_back():
    print("going back")
    pass

commands_lookup = {
    "1": search,
    "2": pause,
    "3": go_back,
    "4": go_next,
}

