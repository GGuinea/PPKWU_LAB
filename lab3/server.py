from flask import Flask, jsonify, request
from bs4 import BeautifulSoup
from ics import Calendar, Event
import requests
import urllib3
import urllib


app = Flask(__name__)

@app.route('/api/check/<string:year>/<sting:month>')
def checkOutput(year, month):
    page = requests.get("http://www.weeia.p.lodz.pl/pliki_strony_kontroler/kalendarz.php?rok="+year+"&miesiac="+month)
    soup = BeautifulSoup(page.content, 'html.parser')

    events = soup.find_all('a', class_='active')
    print(events[0]['href'])

    desc = soup.find_all(class_='InnerBox')
    print(desc[0].getText())

    c = Calendar()
    for i in range(len(events)):
        e = Event()
        e.name = desc[i].getText()
        if int(events[i].getText()) < 10:
            e.begin = '2020-10-0' + events[i].getText() + ' 00:00:00'
        else:
            e.begin = '2020-10-' + events[i].getText() + ' 00:00:00'
        c.events.add(e)

    with open('my.ics', 'w') as my_file:
        my_file.writelines(c)

if __name__ == '__main__':
    app.run(port=25000)
