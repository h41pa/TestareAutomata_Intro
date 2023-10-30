import requests

# ----------- Add User ----------
# url = 'https://thinking-tester-contact-list.herokuapp.com/users'
#
# body_json = {
#     "firstName": "Madalin",
#     "lastName": "Testing",
#     "email": "tester_m@gmail.com",
#     "password": "7654321"
# }
# response = requests.post(url, json=body_json)
# print(response.status_code)

# ----------- Login ----------

url = "https://thinking-tester-contact-list.herokuapp.com/users/login"

body_json = {
    "email": "tester_m@gmail.com",
    "password": "7654321"
}
response =  requests.post(url, json=body_json)
print(response.status_code)

response_json = response.json()

auth_token = response_json['token']

print(response_json['token'])
headers = {
    'Authorization': f'Bearer {auth_token}'
}