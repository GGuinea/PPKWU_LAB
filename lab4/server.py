from flask import Flask, jsonify, request, send_file 
from bs4 import BeautifulSoup
from ics import Calendar, Event
import requests
import urllib3
import json
import urllib

def checkOutput(name):

    page = requests.get("https://panoramafirm.pl/szukaj?k="+name+"&l=")
    soup = BeautifulSoup(page.content, 'html.parser')
    data = soup.find_all('script')
    #3 - 28
    #print(data[27].contents)
    #names = [el['name'] for el in json.loads(data[27].contents.string)['itemListElement']]
    #print(names)
    s = soup.find('script', type='application/ld+json')

    jsonn = json.loads(s.string)
    print(jsonn['name'])

    #k,wprint(soup.find_all("disable"))

checkOutput('Hydraulik')
