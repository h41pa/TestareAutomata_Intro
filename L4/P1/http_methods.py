import requests

# ----------- Add User ----------
# url = 'https://thinking-tester-contact-list.herokuapp.com/users'
#
# body_json = {
#     "firstName": "Madalin",
#     "lastName": "Testing"
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
#
# # ----------- Login ----------
# # ----------- Add Contacts ----------
#
# url = 'https://thinking-tester-contact-list.herokuapp.com/contacts'
# body_json = {
#     "firstName": "John",
#     "lastName": "Doe",
#     "birthdate": "1970-01-01",
#     "email": "jdoe@fake.com",
#     "phone": "8005555555",
#     "street1": "1 Main St.",
#     "street2": "Apartment A",
#     "city": "Anytown",
#     "stateProvince": "KS",
#     "postalCode": "12345",
#     "country": "USA"
# }
# response = requests.post(url, headers=headers, json=body_json)
# print(response.status_code)
# print(response.text)

# ----------- Delete Contacts ----------
# ----------- Get Contact List ----------
url = 'https://thinking-tester-contact-list.herokuapp.com/contacts/653feb16c481ad001364ca65'
response = requests.delete(url, headers=headers)
print(response.status_code)
