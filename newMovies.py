from tkinter import *
from CGVcrawling import *
from LOTTEcrawling import *
from MEGAcrawling import *

def newMovies() :
	win = Tk()
	win.geometry("700x500")
	win.title("recommend new movies")
	win.option_add("*Font", "40")

	dataLab = Label(win, text = "recommend new movies", height = 2)
	dataLab.pack()

	BtCGV = Button(win, text = "CGV", width = 20, heigth = 5)
	BtLOT = Button(win, text = "LOTTE CINEMA", width = 20, height = 5)
	BtMEG = Button(win, text = "MEGA BOX", widht = 20, height = 5)

	def movieCGV():
		CGVcrawling()

	def movieLOT():
		LOTTEcrawling()

	def movieMEG():
		MEGAcrawling()

	BtCGV.config(commend = movieCGV)
	BtCGV.pack()
	BtLOT.config(commend = movieLOT)
	BtLOT.pack()
	BtMEG.config(commend = movieMEG)
	BtMEG.pack()

	win.mainloop()
