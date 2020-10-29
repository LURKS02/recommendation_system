from tkinter import *
from matrix import *
import webbrowser

def matWindow():
	win = Tk()
	win.geometry("700x500")
	win.title("Matrix Factorization")
	win.option_add("*Font", "40")
	
	matLab = Label(win, text = "Matrix Factorization", height = 2)
	matLab.pack()

	movieEnt = Entry(win, width = 30)
	movieEnt.insert(0, "아이디를 입력하세요.")

	def clear(event):
		if movieEnt.get() == "아이디를 입력하세요.":
			movieEnt.delete(0, len(movieEnt.get()))

	movieEnt.pack()
	movieEnt.bind("<Button-1>", clear)

	recommendBtn = Button(win, text = "추천받기")
	recommendBtn.config(width = 20, height = 3)

	movieListBox = Listbox(win, bd = 5, selectbackground = "blue")
	movieListBox.config(width = 50, height = 20)
	movieListBox.pack()

	def ent_p():
		input_id = movieEnt.get()
		movieList = mat_recommend_title(input_id)
		movieListBox.delete(0,9)
		i = 1
		for title in movieList:
			movieListBox.insert(i,title)
			i += 1

	recommendBtn.config(command = ent_p)

	recommendBtn.pack()
	
	win.mainloop()
