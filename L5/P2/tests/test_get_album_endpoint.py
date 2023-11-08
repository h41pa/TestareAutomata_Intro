from L5.P2.requests.spotify_requests import SpotifyRequests
from L5.P2.tests.test_base import TestBase


class TestGetAlbum(TestBase):

    def setUp(self) -> None:
        self.spotify = SpotifyRequests()

    def test_get_album_status_code_and_name(self):
        album_id = '5DkR7Wn2rUWY5Hw9csN0ui'
        response = self.spotify.get_albums(album_id)
        self.verify_status_code(200, response.status_code)
        # expected = 200
        # self.assertEqual(expected, reponse.status_code, "error")

        expected_album = "Fight Back: The Collection"
        self.verify_reponse_size(expected_album, response.json()['name'])
        # print(reponse.json()['name'])

