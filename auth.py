import requests
import os
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv


def authenticate():
    load_dotenv()
    url = "https://accounts.spotify.com/api/token"
    CLIENT_ID = os.getenv("CLIENT_ID")
    CLIENT_SECRET = os.getenv("CLIENT_SECRET")
    payload = {"grant_type": "client_credentials"}
    headers = {"Content-Type" : "application/x-www-form-urlencoded"}
    req = requests.post(url, data=payload, auth=HTTPBasicAuth(CLIENT_ID, CLIENT_SECRET), headers=headers)
    print(req.json())





