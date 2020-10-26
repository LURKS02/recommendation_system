from tkinter import *
from dataWindow import *

mainWin = Tk()
mainWin.geometry("500x270")
mainWin.title("movie recommendation engine")

mainLab = Label(mainWin, text = "추천 방식 선택", height = 2)
mainLab.pack()
dataRec = Button(mainWin, text = "content based filtering", width = 30, height=5)
def contentFiltering():
    dataWindow()
dataRec.config(command = contentFiltering)
dataRec.pack()
mainWin.mainloop()