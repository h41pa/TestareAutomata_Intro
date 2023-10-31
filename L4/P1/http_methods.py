import requests

#----------- Add User ----------
# url = 'https://thinking-tester-contact-list.herokuapp.com/users'
#
# body_json = {
#     "firstName": "Tester",
#     "lastName": "User",
#     "email": "faker@fake.com",
#     "password": "myPassword"
# }
# response = requests.post(url, json=body_json)
# print(response.status_code)


# ----------- Add User ----------

# ----------- Login ----------
url = "https://thinking-tester-contact-list.herokuapp.com/users/login"
body_json = {
    "email": "faker@fake.com",
    "password": "myNewPassword"
}
response = requests.post(url, json=body_json)
print(response.status_code)
reponse_json = response.json()
auth_token = reponse_json['token']
print(reponse_json['token'])
headers = {
    'Authorization': f'Bearer {auth_token}'
}

# ----------- Login ----------

# ----------- Add Contacts ----------
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
#
# response = requests.post(url, json=body_json, headers=headers)
# reponse_json = response.json()
# print(reponse_json['_id'])
# print(response.status_code)
# ----------- Add Contacts ----------

# ----------- Delete Contacts ----------
# url = 'https://thinking-tester-contact-list.herokuapp.com/contacts/654107d5571a650013c9c731'
# response = requests.delete(url, headers=headers)
# print(response.status_code)

# ----------- Delete Contacts ----------

# ----------- Get Contact List ----------
# url = 'https://thinking-tester-contact-list.herokuapp.com/contacts'
# response = requests.get(url, headers=headers)
# print(response.text)

# ----------- Get Contact List ----------

# ----------- Update Contact ----------
# url = 'https://thinking-tester-contact-list.herokuapp.com/contacts/654107a363cab20013cc25b2'
# body_json = {
#     "firstName": "Tester",
#     "lastName": "Fake",
#     "birthdate": "1992-02-02",
#     "email": "amiller@fake.com",
#     "phone": "8005554242",
#     "street1": "13 School St.",
#     "street2": "Apt. 5",
#     "city": "Washington",
#     "stateProvince": "QC",
#     "postalCode": "A1A1A1",
#     "country": "Canada"
# }
# response = requests.put(url, headers=headers, json=body_json)
# print(response.status_code)


# ----------- Update Contact ----------

# ----------- Update Contact - PATCH ----------
# url = 'https://thinking-tester-contact-list.herokuapp.com/contacts/654109ec571a650013c9c732'
# body_json = {
#     "firstName": "Update just fname"
#
# }
# reponse = requests.patch(url, headers=headers, json=body_json)
# print(response.status_code)
# ----------- Update Contact PATCH ----------

# ----------- Get Contact ----------
# url = "https://thinking-tester-contact-list.herokuapp.com/contacts/654109ec571a650013c9c732"
# response = requests.get(url, headers=headers)
# print(response.text)

# ----------- Get Contact ----------

# ----------- Get User Profile ----------
# url = " https://thinking-tester-contact-list.herokuapp.com/users/me"
# response = requests.get(url, headers=headers)
# print(response.text)
# ----------- Get User Profile ----------

# ----------- Update User ----------
# url = "https://thinking-tester-contact-list.herokuapp.com/users/me"
# body_json = {
#     "firstName": "Updated1",
#     "lastName": "Username",
#     "email": "faker@fake.com",
#     "password": "myNewPassword"
# }
# response = requests.patch(url, headers=headers, json=body_json)
# print(response.text)
# # ----------- Update User ----------

# ----------- Logout User ----------
# url = "https://thinking-tester-contact-list.herokuapp.com/users/logout"
# response = requests.post(url, headers=headers)
# print(response.status_code)
# ----------- Logout User ----------


# ----------- Delete User ----------
# url = "https://thinking-tester-contact-list.herokuapp.com/users/me"
# response  =requests.delete(url, headers=headers)
# print(response.status_code)
# ----------- Delete User ----------
