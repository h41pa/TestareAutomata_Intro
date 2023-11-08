from L5.P2.requests.spotify_requests import SpotifyRequests
from L5.P2.tests.test_base import TestBase


class TestNewReleases(TestBase):

    def setUp(self) -> None:
        self.spotify = SpotifyRequests()

    def test_get_new_releases_no_filter(self):
        response = self.spotify.get_new_release()
        expected_code = 200
        actual = response.status_code
        self.assertEqual(expected_code, actual, "Unexpected status code")
        self.verify_status_code(200, response.status_code)
        expected_reponse_size = 20
        actual = len(response.json()['albums']['items'])
        self.assertEqual(expected_reponse_size, actual, "Unexpected size reponse")
        # self.verify_reponse_size(20, response.json()['albums']['items'])

    def test_get_new_releases_filter_by_country(self):
        country = "RO"
        response = self.spotify.get_new_release(country=country)
        item_list = response.json()['albums']['items']
        self.verify_status_code(200, response.status_code)
        self.verify_reponse_size(20, len(item_list))

        for i in range(len(item_list)):
            current_item = item_list[i]
            # name = current_item['name']
            available_markets = current_item['available_markets']
            assert "RO" in available_markets or len(available_markets) == 0
            # # la unele din albume nu avem RO in lista ( posibil bug la spotify in API?)
            # print(f"RO este in lista cu available_markets pentru albumul {name}")



