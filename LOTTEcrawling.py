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
    
req = requests.get('https://www.lottecinema.co.kr/NLCHS/Movies/List?flag=1')
html = req.text
soup = BeautifulSoup(html, 'html.parser')

my_titles = soup.select(
		''
		)

data = {}

for title in my_titles:
	print(title.text)
