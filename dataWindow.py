from tkinter import *

from data import *

win = Tk()
win.geometry("700x500")
win.title("content based filtering")
win.option_add("*Font", "20")

dataLab = Label(win, text = "movie")
dataLab.pack()

movieEnt = Entry(win)
movieEnt.insert(0, "영화 제목을 입력하세요.")
def clear(event):
    if movieEnt.get() == "영화 제목을 입력하세요.":
        movieEnt.delete(0, len(movieEnt.get()))
movieEnt.pack()
movieEnt.bind("<Button-1>", clear)

recommendBtn = Button(win, text="content based filtering")
recommendBtn.config(width = 50, height = 5)

movieListBox = Listbox(win, bd = 5, selectbackground = "blue")
movieListBox.config(width = 50, height = 20)
movieListBox.pack()

def ent_p():
    movieName = movieEnt.get()
    movieList = data_recommend_title(movieName)
    i = 1
    for title in movieList:
        movieListBox.insert(i, title)
        i += 1

recommendBtn.config(command = ent_p)
recommendBtn.pack()


win.mainloop()
