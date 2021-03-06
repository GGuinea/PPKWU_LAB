from flask import Flask, jsonify, request, send_file 
from bs4 import BeautifulSoup
from ics import Calendar, Event
import requests
import urllib3
import urllib


app = Flask(__name__)
app.config["calendar"] = "/my.ics"

@app.route('/api/calendar/<string:year>/<string:month>')
def checkOutput(year, month):
    if int(month) < 10:
        month = '0' + month

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
            e.begin = year + '-' + month + '-0' + events[i].getText() + ' 00:00:00'
            e.make_all_day()
        else:
            e.begin = year + '-' + month + '-' + events[i].getText() + ' 00:00:00'
            e.make_all_day()
        c.events.add(e)

    filename = year + month + ".ics"
    with open(filename, 'w') as my_file:
        my_file.writelines(c)

    return send_file(filename, as_attachment=True)

if __name__ == '__main__':
    app.run(port=25000)
