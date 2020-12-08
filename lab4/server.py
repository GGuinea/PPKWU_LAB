from flask import Flask, jsonify, request, send_file 
from bs4 import BeautifulSoup
from ics import Calendar, Event
import requests
import urllib3
import urllib

def checkOutput(name):

    page = requests.get("https://panoramafirm.pl/szukaj?k="+name+"&l=")
    soup = BeautifulSoup(page.content, 'html.parser')
    print(soup)


checkOutput('Hydraulik')
