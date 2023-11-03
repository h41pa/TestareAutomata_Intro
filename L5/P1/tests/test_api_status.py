from L5.P1.requests.simple_books_requests import SimpleBooksRequests
import unittest


class TestApiStatus(unittest.TestCase):

    def setUp(self) -> None:
        self.books_api = SimpleBooksRequests()

    def test_api_status(self):
        response = self.books_api.get_api_status()

        expected_status_code = 200
        actual_status_code = response.status_code
        self.assertEqual(expected_status_code,actual_status_code), "Error, unexpected status code"

        expected_status_message = "OK"
        actual_status_message = response.json()['status']
        self.assertEqual(expected_status_message, actual_status_message), "Error, unexpected status message"