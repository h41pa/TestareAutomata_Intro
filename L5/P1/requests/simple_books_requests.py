import random
import requests


class SimpleBooksRequests:
    _BASE_URL = "https://simple-books-api.glitch.me"
    _API_STATUS_ENDPOINT = "/status"
    _GET_ALL_BOOKS_ENDPOINT = "/books"
    _API_AUTH_ENDPOINT = "/api-clients/"
    _ORDERS_ENDPOINT = "/orders"


    def get_api_status(self):
        api_status_url = self._BASE_URL + self._API_STATUS_ENDPOINT
        response = requests.get(api_status_url)
        return response

    def get_all_books(self, book_type="", limit=""):
        get_all_books_url = self._BASE_URL + self._GET_ALL_BOOKS_ENDPOINT

        if book_type != "" and limit == "":
            get_all_books_url += f"?type={book_type}"
        elif book_type == "" and limit != "":
            get_all_books_url += f"?limit={limit}"
        elif book_type != "" and limit != "":
            get_all_books_url += f"?type={book_type}&limit={limit}"

        response = requests.get(get_all_books_url)

        return response

    def generate_token(self):
        auth_url = self._BASE_URL + self._API_AUTH_ENDPOINT
        rand_number = random.randint(0, 99999)
        body_json = {
            "clientName": "Mr Madalin",
            "clientEmail": f"madalin{rand_number}@example.com"
        }
        reponse = requests.post(auth_url, json=body_json)
        return reponse.json()["accessToken"]



    def submit_order(self, acces_token, book_id, customer_name):
        submit_orders_url = self._BASE_URL + self._ORDERS_ENDPOINT
        headers_params = {'Authorization': acces_token}
        body_json = {
            "bookId": book_id,
            "customerName": customer_name
        }
        response = requests.post(submit_orders_url, headers=headers_params, json=body_json)
        return response



    def update_order(self, acces_token, order_id, new_costumer_name):
        update_url = self._BASE_URL + self._ORDERS_ENDPOINT + f"/{order_id}"
        header_param = {'Authorization': acces_token}
        body_json = {
            "customerName": new_costumer_name
        }
        response = requests.patch(update_url,headers=header_param, json=body_json )
        return response



