from flask import Flask, jsonify, request, send_file 
from bs4 import BeautifulSoup
from ics import Calendar, Event
import requests
import urllib3
import json
import urllib
import vobject

app = Flask(__name__)

class Company:
    name = ""
    telephone = ""
    email = ""
    url = ""
    address = {}

    def __init__(self, name, telephone, email, url, address):
        self.name = name
        self.telephone = telephone
        self.email = email
        self.url = url
        self.address = address

companies = []

def create_vCard(company):
    card = vobject.vCard()
    card.add('n')
    card.n.value = vobject.vcard.Name(company.name)
    card.add('fn')
    card.fn.value = company.name
    card.add('email')
    card.email.value = company.email
    card.email.type_param = 'INTERNET'
    card.add('org')
    card.org.value = [company.name]
    card.add('tel')
    card.tel.value = company.telephone
    return card


#checkOutput('Hydraulik')
def save_Vcards():
    vcards = []
    for company in companies:
        vcards.append(create_vCard(company))

    i = 0
    for card in vcards:
        print("NAME:",card.n.value)
        print(card.serialize())
        filename = "vcf/company"+str(i)+".vcf"
        i+=1
        with open (filename, 'w') as my_file:
            my_file.writelines(card.serialize())

@app.route('api/vcard/<string:name>')
def checkOutput(name):
    page = requests.get("https://panoramafirm.pl/szukaj?k="+name+"&l=")
    soup = BeautifulSoup(page.content, 'html.parser')
    all_data = soup.find_all('script', type='application/ld+json')
    i = 0
    for script in all_data:
        if i == (len(all_data) -1):
            break
        i+=1
        jsonn = json.loads(script.string)
        companies.append(Company(jsonn['name'], jsonn['telephone'], jsonn['email'], jsonn['url'], jsonn['address']))
    save_Vcards()



if __name__ == '__main__':
    app.run(port=25000)
