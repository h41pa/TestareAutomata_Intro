import unittest
from L5.P1.requests.simple_books_requests import SimpleBooksRequests


class TestUpdateOrder(unittest.TestCase):
    acces_token = ""

    def setUp(self):
        self.books_api = SimpleBooksRequests()

        if self.acces_token == "":
            self.acces_token =  self.books_api.generate_token()

    def test_update_order_status_code(self):
        book_id = 1
        customer_name = "Dementor"
        place_order_resp = self.books_api.submit_order(self.acces_token, book_id, customer_name)
        status_code =  201
        expected_status = place_order_resp.status_code
        self.assertEqual(status_code, expected_status, " Error , unexpected statsu code")
        order_id = place_order_resp.json()['orderId']
        new_costumer_name = "Bujie"
        update_order_resp = self.books_api.update_order(self.acces_token, order_id, new_costumer_name)
        expected_status_code = 204
        actual_Status_code = update_order_resp.status_code
        self.assertEqual(expected_status_code, actual_Status_code, "Error , unexpected status")
