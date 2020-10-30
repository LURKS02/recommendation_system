from tkinter import *
import requests
from bs4 import BeautifulSoup

class movieInfo :
    title = ''
    reservation = ''
    poster = ''
    date = ''

    def __init__(self, title, reservation, poster, date):
        self.title = title
        self.reservation = reservation
        self.poster = poster
        self.date = date

# CGV 영화 차트 홈페이지에서 크롤링을 진행
# 영화 제목, 예매율, 포스터, 개봉일자 정보를 받아옴
def crawling() :
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

    my_titles_info = soup.select(
	    'ol > li > div.box-contents > a > strong.title'
	)
    my_titles = []
    for title in my_titles_info:
        my_titles.append(title.text)

    my_reservations_info = soup.select(
        'ol > li > div.box-contents > div.score > strong.percent > span'
    )
    my_reservations = []
    for reservation in my_reservations_info:
        my_reservations.append(reservation.text)

    my_images_info = soup.select('ol > li > div.box-image > a > span.thumb-image > img[src]')
    my_posters = []
    for image in my_images_info:
        my_posters.append(image['src'])

    my_dates_info = soup.select(
        'ol > li > div.box-contents > span.txt-info > strong'
    )
    my_dates = []
    for date in my_dates_info:
        my_dates.append(date.text.replace(" ", "").strip())

    classList = []
    for i in range(len(my_titles)):
        newClass = movieInfo(my_titles[i], my_reservations[i], my_posters[i], my_dates[i])
        classList.append(newClass)

    return classList
