from flask import Flask, jsonify, request, send_file 
from bs4 import BeautifulSoup
from ics import Calendar, Event
import requests
import urllib3
import json
import urllib

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

checkOutput('Hydraulik')
print(companies[24].name)

