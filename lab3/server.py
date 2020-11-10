from flask import Flask, jsonify, request
from bs4 import BeautifulSoup
import requests
import urllib3
import urllib

page = requests.get("http://www.weeia.p.lodz.pl/pliki_strony_kontroler/kalendarz.php")
print(page)
print(page.content)
soup = BeautifulSoup(page.content, 'html.parser')
print(soup.prettify())
