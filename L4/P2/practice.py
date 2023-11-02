import json

from flask import Flask, request

app = Flask(__name__)

contact = {}

@app.route('/afiseaza_agenda', methods=['GET'])
def afiseaza_agenda():
    if bool(contact):
        json_object = json.dumps(contact)
        return json_object
    else:
        return {'message': 'No contacts has been found'}

"""
{
 "name": "Madalin",
 "phone": "0733123456"
}
"""
@app.route('/creaza_contact', methods=['POST'])
def creaza_contact():
    phone_number = request.json['phone']
    contact_name = request.json['name']
    if phone_number not in contact.items():
        contact.update({contact_name: phone_number})
        json_object = json.dumps(contact)
        return json_object
    else:
        return {'message': 'That contact already exists in your phonebook'}


"""
{
 "name": "Madalin",

}
"""
@app.route('/Verifica_contact', methods=['GET'])
def verifica_contact():
    nume = request.json['name']

    if nume in contact:
        return {'Name': nume, 'phone': contact[nume]}
    else:
        return {'message': 'That contact does not exist!!'}


@app.route('/sterge_contact', methods=['DELETE'])
def sterge_contact():
    nume = request.json['name']
    if nume in contact:
        contact.pop(nume, None)
        json_obj = json.dumps(contact)
        return json_obj
    else:
        return {'message': 'Contactul nu exsita'}

if __name__ == "__main__":
    app.run()


