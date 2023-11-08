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

        submit_order_reponse = self.books_api.submit_order(self.acces_token, book_id, customer_name)
        expected_status_code = 201
        actual_status_code = submit_order_reponse.status_code
        self.assertEqual(expected_status_code, actual_status_code, "Error, Not created")
        order_id = submit_order_reponse.json()['orderId']
        new_customer_name = "Daniel"
        update_order_response = self.books_api.update_order(self.acces_token, order_id, new_customer_name)
        expected_status_code = 204
        actual_status_code = update_order_response.status_code
        self.assertEqual(expected_status_code, actual_status_code, "Unexpected Status Code")


