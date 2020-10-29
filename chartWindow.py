from tkinter import *
from CGVcrawling import *
from PIL import ImageTk, Image
import os
from io import BytesIO
from urllib.request import urlopen
import base64

def imgCrawling(url):
    u = urlopen(url)
    raw_data = u.read()
    u.close()

    im = Image.open(BytesIO(raw_data))
    im = im.resize((350, 500))
    return im

def chartWindow():
    chartWin = Tk()
    chartWin.geometry("1400x1000+100+100")
    chartWin.title("movie chart")
    chartWin.option_add("*Font", "40")
    classList = crawling()

    URL0 = classList[0].poster
    photo0 = ImageTk.PhotoImage(imgCrawling(URL0), master = chartWin)
    label0 = Label(chartWin, image=photo0)
    label0.image = photo0
    label0.grid(row=0, column=0)

    URL1 = classList[1].poster
    photo1 = ImageTk.PhotoImage(imgCrawling(URL1), master=chartWin)
    label1 = Label(chartWin, image=photo1)
    label1.image = photo1
    label1.grid(row=0, column=1)

    URL2 = classList[2].poster
    photo2 = ImageTk.PhotoImage(imgCrawling(URL2), master=chartWin)
    label2 = Label(chartWin, image=photo2)
    label2.image = photo2
    label2.grid(row=0, column=2)

    URL3 = classList[3].poster
    photo3 = ImageTk.PhotoImage(imgCrawling(URL3), master=chartWin)
    label3 = Label(chartWin, image=photo3)
    label3.image = photo3
    label3.grid(row=0, column=3)

    URL4 = classList[4].poster
    photo4 = ImageTk.PhotoImage(imgCrawling(URL4), master=chartWin)
    label4 = Label(chartWin, image=photo4)
    label4.image = photo4
    label4.grid(row=1, column=0)

    URL5 = classList[5].poster
    photo5 = ImageTk.PhotoImage(imgCrawling(URL5), master=chartWin)
    label5 = Label(chartWin, image=photo5)
    label5.image = photo5
    label5.grid(row=1, column=1)

    URL6 = classList[6].poster
    photo6 = ImageTk.PhotoImage(imgCrawling(URL6), master=chartWin)
    label6 = Label(chartWin, image=photo6)
    label6.image = photo6
    label6.grid(row=1, column=2)

    chartWin.mainloop()