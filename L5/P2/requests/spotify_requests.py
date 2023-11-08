import requests
from requests_oauth2client import *


# install pip install requests-oauth2client

class SpotifyRequests:
    _BASE_URL = "https://api.spotify.com/v1"
    _TOKEN_ENDPOINT = "https://accounts.spotify.com/api/token"
    _GET_ALBUM_ENDPOINT = "/albums/"
    _GET_PLAYlIST_ENDPOINT = "/playlists/"
    _GET_NEW_RELEASES_ENDPOINT = "/browse/new-releases"
    _AUTH_CLIENT_SECRET_AND_PASSWORD = ("f373bd3cfd4f4d47945ead29af02d675", "a131989ad88f4ec88ad6d7f59b12c5d1")
    _CALLBACK_URI = "http://testmyspotifyapp13"
    _TOKEN = ""
    _SCOPES = "ugc-image-upload user-read-playback-state user-modify-playback-state user-read-currently-playing " \
              "app-remote-control streaming playlist-read-private playlist-read-collaborative " \
              "playlist-modify-private playlist-modify-public user-follow-modify user-follow-read " \
              "user-read-playback-position user-top-read user-read-recently-played user-library-modify " \
              "user-library-read user-read-email user-read-private"

    _GET_USER = "/me"

    def __init__(self):
        self.generate_token()

    def generate_token(self):
        if len(self._TOKEN) < 1:
            # Instatam un client prin care obtinem token-ul
            # Clientul primeste ca parametri:
            # - token_endpoint - endpointul de generare al tokenului
            # - auth - tupla format client id si client secret
            oauth2client = OAuth2Client(token_endpoint=self._TOKEN_ENDPOINT, auth=self._AUTH_CLIENT_SECRET_AND_PASSWORD)
            self._TOKEN = f"Bearer {oauth2client.client_credentials(scope=self._SCOPES, resource=self._CALLBACK_URI)}"
            print(self._TOKEN)

    def get_token(self):
        return self._TOKEN

    def get_headers_params(self):
        return {'Authorization': self.get_token()}

    def get_albums(self, album_id):
        album_endpoint = self._BASE_URL + self._GET_ALBUM_ENDPOINT + f'{album_id}'
        response = requests.get(album_endpoint, headers=self.get_headers_params())
        return response

    def get_new_release(self, country="", limit=""):
        new_releases_endpoint = self._BASE_URL + self._GET_NEW_RELEASES_ENDPOINT
        if country != "" and limit == "":
            new_releases_endpoint += f'?country={country}'
        elif country == "" and limit != "":
            new_releases_endpoint += f'?limit={limit}'
        elif country != "" and limit != "":
            new_releases_endpoint += f'?country={country}&limit={limit}'

        response = requests.get(new_releases_endpoint, headers=self.get_headers_params())
        return response

    def get_playlist(self, playlist_id):
        playlist_endpoint = self._BASE_URL + self._GET_PLAYlIST_ENDPOINT + f'{playlist_id}'
        response = requests.get(playlist_endpoint, headers=self.get_headers_params())
        return response

    # def add_item_in_playlist(self, playlist_id, track_id, position):
    #     add_endpoint = self._BASE_URL + self._GET_PLAYlIST_ENDPOINT + f"{playlist_id}/tracks"
    #
    #     body_json = {
    #         "uris": [
    #             f"spotify:track:{track_id}"
    #         ],
    #         "position": position
    #     }
    #     response = requests.post(add_endpoint, headers=self.get_headers_params(), data=body_json)
    #     return response
    #

    # def get_id(self):
    #     get_id = self._BASE_URL + self._GET_USER
    #     reponse_id = requests.get(get_id, headers=self.get_headers_params())
    #     return reponse_id

    def create_playlist(self, playlist_name, description, public):

        create_playlist_endpoint = f"https://api.spotify.com/v1/users/{self.get_id()}/playlists"

        body_json = {
            "name": playlist_name,
            "description": description,
            "public": public
        }
        response = requests.post(create_playlist_endpoint, headers=self.get_headers_params(), json=body_json)
        return response


spotify = SpotifyRequests()
spotify.generate_token()
