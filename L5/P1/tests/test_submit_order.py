import unittest
from L5.P1.requests.simple_books_requests import SimpleBooksRequests


class TestSubmitOrder(unittest.TestCase):
    access_token = ""

    def setUp(self):
        self.books_api = SimpleBooksRequests()

        if self.access_token == "":
            self.access_token = self.books_api.generate_token()

    def test_submit_order_status_code(self):
        book_id = 1
        customer_name = "Dementor"

        response = self.books_api.submit_order(self.access_token, book_id, customer_name)

        expected_status_code = 201
        actual_status_code = response.status_code

        self.assertEqual(expected_status_code, actual_status_code, "Error, unexpected status code")
        expected_created_message = True
        actual_created_message = response.json()['created']
        self.assertEqual(expected_created_message, actual_created_message, "Error , unexpected message ")

    def test_submit_order_with_invalid_book_id(self):
        book_id = 999
        customer_name = "Decu"
        response = self.books_api.submit_order(self.access_token, book_id, customer_name)
        expected_status_code = 400
        actual_status_code = response.status_code
        self.assertEqual(expected_status_code, actual_status_code, "Error, Unexpected status code")

        expected_error_message = "Invalid or missing bookId."
        actual_error_mesagge = response.json()['error']
        self.assertEqual(expected_error_message, actual_error_mesagge, "Error, unexpected message ")