from tkinter import *
from dataWindow import *
from matWindow import *
from chartWindow import *

mainWin = Tk()
mainWin.geometry("500x330")
mainWin.title("movie recommendation engine")

mainLab = Label(mainWin, text = "추천 방식 선택", height = 2)
mainLab.pack()

dataRec = Button(mainWin, text = "Content Based Filtering", width = 30, height=5)
matRec = Button(mainWin, text = "Matrix Factorization", width = 30, height = 5)
chartRec = Button(mainWin, text = "Movie Chart", width = 30, height = 5)

def contentFiltering():
    dataWindow()

def matrixfactorization():
	matWindow()

def movieChart():
    chartWindow()

dataRec.config(command = contentFiltering)
dataRec.pack()

matRec.config(command = matrixfactorization)
matRec.pack()

chartRec.config(command = movieChart)
chartRec.pack()

mainWin.mainloop()
