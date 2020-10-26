from tkinter import *

from data import *

win = Tk()
win.geometry("700x500")
win.title("content based filtering")
win.option_add("*Font", "40")

dataLab = Label(win, text = "content based filtering", height = 2)
dataLab.pack()

movieEnt = Entry(win)
movieEnt.insert(0, "영화 제목을 입력하세요.")
def clear(event):
    if movieEnt.get() == "영화 제목을 입력하세요.":
        movieEnt.delete(0, len(movieEnt.get()))
movieEnt.pack()
movieEnt.bind("<Button-1>", clear)

recommendBtn = Button(win, text="추천받기")
recommendBtn.config(width = 20, height = 3)

movieListBox = Listbox(win, bd = 5, selectbackground = "blue")
movieListBox.config(width = 50, height = 20)
movieListBox.pack()

def ent_p():
    movieName = movieEnt.get()
    movieList = data_recommend_title(movieName)
    movieListBox.delete(0,9)
    i = 1
    for title in movieList:
        movieListBox.insert(i, title)
        i += 1

recommendBtn.config(command = ent_p)

def movieInfo(event):
    selected = movieListBox.selection_get()
    subWin = Tk()
    subWin.geometry("400x300")
    subWin.title("movie information")
    subWinLab01 = Label(subWin, text = "영화 정보", font = "맑은고딕 15")
    subWinLab01.config(height = 5)
    selectedInfo = movie_info(selected, movieEnt.get())
    subWinLab02 = Label(subWin, text = "id : " + selectedInfo.iloc[0]['id'])
    subWinLab03 = Label(subWin, text = "title : " + selectedInfo.iloc[0]['title'])
    subWinLab04 = Label(subWin, text = "genres : " + selectedInfo.iloc[0]['genres'])
    subWinLab05 = Label(subWin, text = "popularity : " + str(selectedInfo.iloc[0]['popularity']))
    subWinLab06 = Label(subWin, text = "vote_average : " + str(selectedInfo.iloc[0]["vote_average"]))
    subWinLab07 = Label(subWin, text = "vote_count : " + str(selectedInfo.iloc[0]["vote_count"]))
    subWinLab08 = Label(subWin, text = "score : " + str(selectedInfo.iloc[0]["score"]))

    subWinLab01.pack()
    subWinLab02.pack()
    subWinLab03.pack()
    subWinLab04.pack()
    subWinLab05.pack()
    subWinLab06.pack()
    subWinLab07.pack()
    subWinLab08.pack()

movieListBox.bind('<Double-Button-1>',movieInfo)
recommendBtn.pack()


win.mainloop()
