from tkinter import *
from dataWindow import *
from matWindow import *

mainWin = Tk()
mainWin.geometry("500x270")
mainWin.title("movie recommendation engine")

mainLab = Label(mainWin, text = "추천 방식 선택", height = 2)
mainLab.pack()

dataRec = Button(mainWin, text = "content based filtering", width = 30, height=5)
matRec = Button(mainWin, text = "Matrix Factorization", width = 30, height = 5)

def contentFiltering():
    dataWindow()

def matrixfactorization():
	matWindow()

dataRec.config(command = contentFiltering)
dataRec.pack()

matRec.config(command = matrixfactorization)
matRec.pack()

mainWin.mainloop()
