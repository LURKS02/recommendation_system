from tkinter import *
from CGVcrawling import *
from PIL import ImageTk, Image
import os
from io import BytesIO
from urllib.request import urlopen
import base64
from functools import partial

# url에서 이미지 정보를 받아오는 과정
def imgCrawling(url):
    u = urlopen(url)
    raw_data = u.read()
    u.close()

    im = Image.open(BytesIO(raw_data))
    im = im.resize((350, 500))
    return im


# movie chart의 영화 상세보기 창 구현
def chartInfo(title, reservation, poster, date):
    subWin = Tk()
    subWin.geometry("600x660")
    subWin.title("movie information")
    subWinLab01 = Label(subWin, text="<Movie Information>", font="맑은고딕 10")
    subWinLab02 = Label(subWin, text="title : " + title)
    subWinLab03 = Label(subWin, text="reservation : " + reservation)
    photo = ImageTk.PhotoImage(imgCrawling(poster), master=subWin)
    subWinLab04 = Label(subWin, image=photo)
    subWinLab04.image = photo
    subWinLab05 = Label(subWin, text="date : " + date)

    subWinLab01.pack()
    subWinLab02.pack()
    subWinLab03.pack()
    subWinLab04.pack()
    subWinLab05.pack()
    subWin.mainloop()

# 웹 크롤링을 통해 받아온 정보는 class 형태로 classList에 저장
# 각 요소에 대해 버튼을 생성하고 class정보를 받아와 chartInfo의 인수로 넘겨줌
def chartWindow():
    chartWin = Tk()
    chartWin.geometry("1400x1000+100+100")
    chartWin.title("movie chart")
    chartWin.option_add("*Font", "40")
    classList = crawling()

    URL0 = classList[0].poster
    photo0 = ImageTk.PhotoImage(imgCrawling(URL0), master = chartWin)
    label0 = Button(chartWin, image=photo0)
    label0.image = photo0
    label0.config(command = partial(chartInfo, classList[0].title, classList[0].reservation, classList[0].poster, classList[0].date))
    label0.grid(row=0, column=0)

    URL1 = classList[1].poster
    photo1 = ImageTk.PhotoImage(imgCrawling(URL1), master=chartWin)
    label1 = Button(chartWin, image=photo1)
    label1.image = photo1
    label1.config(command = partial(chartInfo, classList[1].title, classList[1].reservation, classList[1].poster, classList[1].date))
    label1.grid(row=0, column=1)

    URL2 = classList[2].poster
    photo2 = ImageTk.PhotoImage(imgCrawling(URL2), master=chartWin)
    label2 = Button(chartWin, image=photo2)
    label2.image = photo2
    label2.config(command = partial(chartInfo, classList[2].title, classList[2].reservation, classList[2].poster, classList[2].date))
    label2.grid(row=0, column=2)

    URL3 = classList[3].poster
    photo3 = ImageTk.PhotoImage(imgCrawling(URL3), master=chartWin)
    label3 = Button(chartWin, image=photo3)
    label3.image = photo3
    label3.config(command = partial(chartInfo, classList[3].title, classList[3].reservation, classList[3].poster, classList[3].date))
    label3.grid(row=0, column=3)

    URL4 = classList[4].poster
    photo4 = ImageTk.PhotoImage(imgCrawling(URL4), master=chartWin)
    label4 = Button(chartWin, image=photo4)
    label4.image = photo4
    label4.config(command = partial(chartInfo, classList[4].title, classList[4].reservation, classList[4].poster, classList[4].date))
    label4.grid(row=1, column=0)

    URL5 = classList[5].poster
    photo5 = ImageTk.PhotoImage(imgCrawling(URL5), master=chartWin)
    label5 = Button(chartWin, image=photo5)
    label5.image = photo5
    label5.config(command = partial(chartInfo, classList[5].title, classList[5].reservation, classList[5].poster, classList[5].date))
    label5.grid(row=1, column=1)

    URL6 = classList[6].poster
    photo6 = ImageTk.PhotoImage(imgCrawling(URL6), master=chartWin)
    label6 = Button(chartWin, image=photo6)
    label6.image = photo6
    label6.config(command = partial(chartInfo, classList[6].title, classList[6].reservation, classList[6].poster, classList[6].date))
    label6.grid(row=1, column=2)

    chartWin.mainloop()