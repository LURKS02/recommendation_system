from tkinter import *
import requests
from bs4 import BeautifulSoup

requests.packages.urllib3.disable_warnings()
requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS += ':HIGH:!DH:!aNULL'
try:
    requests.packages.urllib3.contrib.pyopenssl.util.ssl_.DEFAULT_CIPHERS += ':HIGH:!DH:!aNULL'
except AttributeError:
    # no pyopenssl support used / needed / available
    pass
    
req = requests.get('http://megabox.co.kr/movie')
html = req.text
soup = BeautifulSoup(html, 'html.parser')
table = soup.find(id = "contents")
movies = table.find_all(class_="title")

for movie in movies:
	title = movie.get_text()
	print(title, end=' ')
