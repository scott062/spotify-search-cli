import requests
import os
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv


def authenticate():
    load_dotenv()

    CLIENT_ID = os.getenv("CLIENT_ID")
    CLIENT_SECRET = os.getenv("CLIENT_SECRET")

    url = "https://accounts.spotify.com/api/token"
    payload = {"grant_type": "client_credentials"}
    headers = {"Content-Type" : "application/x-www-form-urlencoded"}

    res = requests.post(url, data=payload, auth=HTTPBasicAuth(CLIENT_ID, CLIENT_SECRET), headers=headers)

    if res.ok:
        token = res.json().get("access_token")
        write_token(token)
        return read_token()
    return res.raise_for_status()

def write_token(token):
    with open("token.txt", "w") as f:
        f.write(token)

def read_token():
    with open("token.txt", "r") as f:
        content = f.read()
        return content


