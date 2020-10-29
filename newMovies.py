from tkinter import *
import requests

requests.packages.urllib3.disable_warnings()
requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS += ':HIGH:!DH:!aNULL'
try:
    requests.packages.urllib3.contrib.pyopenssl.util.ssl_.DEFAULT_CIPHERS += ':HIGH:!DH:!aNULL'
except AttributeError:
    # no pyopenssl support used / needed / available
    pass
    
def newMovies() :
	win = Tk()
	win.geometry("700x500")
	win.title("recommend new movies")
	win.option_add("*Font", "40")

	req = requests.get('https://cgv.co.kr/movies/')
	html = req.text
	soup = BeautifulSoup(html, 'html.parser')

	my_titles = soup.select(
		'ol > li > div.box-contents > a > strong.title'
		)

	data = {}

	for title in my_titles:
		print(title.text)
	
	win.mainloop()
