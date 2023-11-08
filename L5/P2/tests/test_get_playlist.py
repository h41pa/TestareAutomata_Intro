from L5.P2.requests.spotify_requests import SpotifyRequests
from L5.P2.tests.test_base import TestBase


class TestPlaylist(TestBase):

    def setUp(self):
        self.spotify = SpotifyRequests()

    def test_get_playlist(self):
        playlist_id = "3pQBjhHv3cQTnnHxtL56Zn"
        reponse = self.spotify.get_playlist(playlist_id)
        self.verify_status_code(200, reponse.status_code)
        tracks = reponse.json()['tracks']['items']
        # actual playlist have 3 tracks
        self.verify_reponse_size(3, len(tracks))

    # def test_add_track(self):
    #
    #     playlist_id = "3pQBjhHv3cQTnnHxtL56Zn"
    #     track_id = "3MjExYRhoVn6yhd3fk3gUO"
    #     position = 3
    #     response = self.spotify.add_item_in_playlist(playlist_id=playlist_id, track_id=track_id, position=position)
    #     # self.verify_status_code(201, response.status_code)
    #     print(response.json())

    # def test_id(self):
    #     response = self.spotify.get_id()
    #     print(response.json)

    # def test_create_playlist(self):
    #     name = "test"
    #     description = "lalal"
    #     public = False
    #     response = self.spotify.create_playlist(name, description, public)
    #
    #     print(response.json())
