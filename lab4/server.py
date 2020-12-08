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
    all_data = soup.find_all('script', type='application/ld+json')
    for script in all_data:
        jsonn = json.loads(script.string)
        print(jsonn['name'])

checkOutput('Hydraulik')
