import requests
import os
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv
from constants import API_TOKEN


class RequestsSession:
    def __init__(self):
        self.token = None
        self.session = requests.Session()
        if not self.token:
            self.token = self.__get_token__()
        self.session.headers.update({"Authorization": f"Bearer {self.token}", "accept": "application/json"})

    def get(self, url, **kwargs):
        return self.session.get(url, **kwargs)

    def post(self, url, data=None, json=None, **kwargs):
        return self.session.post(url, data=data, json=json, **kwargs)

    def __get_token__(self):
        load_dotenv()

        CLIENT_ID = os.getenv("CLIENT_ID")
        CLIENT_SECRET = os.getenv("CLIENT_SECRET")

        payload = {"grant_type": "client_credentials"}
        headers = {"Content-Type" : "application/x-www-form-urlencoded"}

        try:
            # Not using the session yet, using vanilla requests to get initial token
            res = requests.post(API_TOKEN, data=payload, auth=HTTPBasicAuth(CLIENT_ID, CLIENT_SECRET), headers=headers)
            res.raise_for_status()
            return res.json().get("access_token")
        except Exception as e:
            print(f"Error loading token: {e}")


