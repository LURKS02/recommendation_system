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
    
req = requests.get('https://cgv.co.kr/movies/')
html = req.text
soup = BeautifulSoup(html, 'html.parser')

my_titles = soup.select(
		'ol > li > div.box-contents > a > strong.title'
		)

data = {}

for title in my_titles:
	print(title.text)
