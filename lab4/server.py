from flask import Flask, jsonify, request, send_file 
from bs4 import BeautifulSoup
from ics import Calendar, Event
import requests
import urllib3
import json
import urllib
import vobject

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


checkOutput('Hydraulik')
vcards = []
for company in companies:
    vcards.append(create_vCard(company))

for card in vcards:
    print(card.prettyPrint())
    print(card.serialize())

filename = "example.vcard"
with open (filename, 'w') as my_file:
    my_file.writelines(vcards[1].serialize())

