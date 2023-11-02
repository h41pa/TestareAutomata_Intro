# """
# ce este un web framework: ne ajuta sa construim un web API
#
# Flask - micro web framework - este foarte lightwieight
#
# Nota: FastAPI  - ( alt framework mai rapid ca flask) ###################
#
# """

# from flask import Flask

# Cream o aplicatie Flask, careia ii dam numele  __name__ => numele fisierului curent
# app = Flask(__name__)


# @app.route('/')
# def index():
#     return "Main Page"
#
#
# @app.route('/page1')
# def hello():
#     return "Hello this is page 1"


# """
# 127.0.0.1 = o adresa IP care simbolizeaza calculatorul nostru
# 5000 = portul pe care ruleaza serverul nostru
# IP:PORT = Socket
# """

# @app.route('/hello/<nume>')
# def hello_nume(nume):
#     return f"salut {nume} !"
#
#
# @app.route('/test/<name>')
# def hello_name(name):
#     return f'Hello {name}'
#
#
# if __name__ == "__main__":
#     app.run()

import json
from flask import Flask, request

app = Flask(__name__)

contact = {}


@app.route('/display_phonebook', methods=['GET'])
def display_phonebook():
    # Check if contact is empty
    if bool(contact):
        json_object = json.dumps(contact)
        return json_object
    # Else inform the user that phonebook is empty
    else:
        return {'message': 'You have an empty phonebook!'}


"""
{
 "name": "Madalin",
 "phone": "0733123456"
}
"""


@app.route('/create_contact', methods=['POST'])
def create_contact():
    # Request for phone number and contact name
    phone_number = request.json['phone']
    contact_name = request.json['name']

    # Check if the contact number already exists in phonebook
    if phone_number not in contact.items():
        contact.update({contact_name: phone_number})
        json_object = json.dumps(contact)
        return json_object
    # Else display message to inform user that contact already exists
    else:
        return {'message': 'That contact already exists in your phonebook'}


"""
{
 "name": "Madalin"
}
"""


@app.route('/check_contact', methods=['GET'])
def check_contact():
    name = request.json['name']
    # Create a condition to check if the entered name is in the phonebook
    if name in contact:
        return {"name": name, 'phone': contact[name]}
    # Else display message to inform user that contact does not exists
    else:
        return {'message': 'That contact does not exist!!'}


"""
{
 "name": "Madalin"
}
"""


@app.route('/delete_contact', methods=['DELETE'])
def delete_contact():
    name = request.json['name']
    # Create a condition to check if the entered name is in the phonebook
    if name in contact:
        # If contact exists, delete contact
        contact.pop(name, None)
        json_object = json.dumps(contact)
        return json_object
    # Else display message to inform user that contact does not exists
    else:
        return {'message': 'That contact does not exist!!'}


if __name__ == '__main__':
    app.run()
