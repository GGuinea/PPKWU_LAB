from flask import Flask, jsonify, request
from bs4 import BeautifulSoup
from ics import Calendar, Event
import requests
import urllib3
import urllib

page = requests.get("http://www.weeia.p.lodz.pl/pliki_strony_kontroler/kalendarz.php?rok=2020&miesiac=10")
soup = BeautifulSoup(page.content, 'html.parser')
print(soup)
days = soup.find_all('a')
day = 2
lastDay = len(days)-1

events = soup.find_all('a', class_='active')
print(events[0]['href'])

desc = soup.find_all(class_='InnerBox')
print(desc[0].getText())

c = Calendar()
e = Event()
for i in range(len(events)):
    e.name = desc[i].getText()
    if int(events[i].getText()) < 10:
        e.begin = '2020-10-0' + events[i].getText() + ' 00:00:00'
    else:
        e.begin = '2020-10-' + events[i].getText() + ' 00:00:00'
    c.events.add(e)

print(c.events)
