import cmd
import json
from auth import RequestsSession
from constants import SEARCH_TYPES, API_SEARCH, API_ALBUMS, API_ARTISTS, API_TRACKS, API_PLAYLISTS
from helpers import filter_json_data

class SpotifyCLI(cmd.Cmd):
    prompt = ">> "
    intro = "Welcome to Scotty's Spotify CLI"

    def __init__(self):
        super().__init__()
        self.session = RequestsSession()
        self.api_type = "search"

    # ---------Initialization & Cleanup---------
    def postloop(self):
        self.session = None

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
    def do_artist(self, artist_name):
        """
        Search spotify for artist using: artist <artist name>
        """

        res = self.session.get(API_SEARCH, params={
            "type": "artist",
            "q": artist_name,
            "limit": 3
        }).json()

        _res = res.get("artists").get("items")

        fields_to_return = {
            "name",
            "popularity",
            "genres"
        }
        print(json.dumps(list(filter_json_data(_res, fields_to_return)), indent=4))


    def do_album(self, album_name):
        """
        Search spotify for album using: album <album name>
        """
        res = self.session.get(API_SEARCH, params={
            "type": "album",
            "q": album_name,
            "limit": 3
        }).json()

        _res = res.get("albums").get("items")

        fields_to_return = {
            "name",
            "release_date",
            "total_tracks"
        }
        print(json.dumps(list(filter_json_data(_res, fields_to_return)), indent=4))


    def do_song(self, song_name):
        """
        Search spotify for song: song <song name>
        """
        res = self.session.get(API_SEARCH, params={
            "type": "track",
            "q": song_name,
            "limit": 3
        }).json()

        _res = res.get("tracks").get("items")

        fields_to_return = {
            "name": None,
            "album": {
                "name": None
            },
            "artists": {
                "name": None
            },
            "popularity": None
        }
        print(json.dumps(list(filter_json_data(_res, fields_to_return)), indent=4))


    def do_playlist(self, playlist_name):
        """
        Search spotify for playlist: playlist <playlist name>
        """
        res = self.session.get(API_SEARCH, params={
            "type": "playlist",
            "q": playlist_name,
            "limit": 3
        }).json()

        _res = res.get("playlists").get("items")

        fields_to_return = {
            "name",
            "popularity",
            "genres"
        }
        print(json.dumps(list(filter_json_data(_res, fields_to_return)), indent=4))

