from flask import Flask, jsonify, request
from bs4 import BeautifulSoup
import requests
import urllib3
import urllib

page = requests.get("http://www.weeia.p.lodz.pl/pliki_strony_kontroler/kalendarz.php?rok=2020&miesiac=10")
soup = BeautifulSoup(page.content, 'html.parser')
print(soup)
days = soup.find_all('a')
day = 2
while day <= len(days)-1:
    print(days[day].getText())
    day += 1

events = soup.find_all('a', class_='active')
print(events[0]['href'])
