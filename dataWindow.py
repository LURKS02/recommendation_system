from tkinter import *
import webbrowser
from data import *

def dataWindow() :
    win = Tk()
    win.geometry("700x500")
    win.title("content based filtering")
    win.option_add("*Font", "40")

    dataLab = Label(win, text = "content based filtering", height = 2)
    dataLab.pack()

    movieEnt = Entry(win, width = 30)
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

    # 입력창에 입력된 영화 제목을 토대로
    # title에 대한 영화 추천 함수를 실행하여 영화 리스트를 받아옴
    def ent_p():
        movieName = movieEnt.get()
        movieList = data_recommend_title(movieName)
        movieListBox.delete(0,9)
        i = 1
        for title in movieList:
            movieListBox.insert(i, title)
            i += 1

    recommendBtn.config(command = ent_p)

    # 추천된 영화 리스트의 각 영화에 대한 상세보기 창을 구현
    # dataset에서 해당 영화에 관련된 정보를 추출하여 표시함
    def movieInfo(event):
        selected = movieListBox.selection_get()
        subWin = Tk()
        subWin.geometry("600x420")
        subWin.title("movie information")
        subWinLab01 = Label(subWin, text = "<Movie Information>", font = "맑은고딕 10")
        selectedInfo = movie_info(selected, movieEnt.get())
        movieURL = "https://www.imdb.com/title/" + selectedInfo.iloc[0]['imdb_id']

        subWinLab02 = Label(subWin, text = "id : " + selectedInfo.iloc[0]['id'])
        subWinLab03 = Label(subWin, text = "title : " + selectedInfo.iloc[0]['title'])
        subWinLab04 = Label(subWin, text = "genres : " + selectedInfo.iloc[0]['genres'])
        subWinLab05 = Label(subWin, text = "popularity : " + str(selectedInfo.iloc[0]['popularity']))
        subWinLab06 = Label(subWin, text = "vote_average : " + str(selectedInfo.iloc[0]["vote_average"]))
        subWinLab07 = Label(subWin, text = "vote_count : " + str(selectedInfo.iloc[0]["vote_count"]))
        subWinLab08 = Label(subWin, text = "score : " + str(selectedInfo.iloc[0]["score"]))
        subWinLab09 = Label(subWin, text = "overview : " + selectedInfo.iloc[0]["overview"])
        subWinLab10 = Label(subWin, text = selectedInfo.iloc[0]["tagline"], font = "Courier 11")
        subWinLab11 = Label(subWin, text = selectedInfo.iloc[0]["title"], font = "Times 17")

        def callback(url):
            webbrowser.open_new(url)

        subWinLab12 = Label(subWin, text = movieURL, fg="blue", cursor="hand2")
        subWinLab12.bind("<Button-1>", lambda e: callback(movieURL))
        subWinLab10.config(wraplength=400)
        subWinLab09.config(wraplength=400)
        subWinLab10.config(height = 2)
        subWinLab11.config(height = 2)


        subWinLab01.pack()

        subWinLab11.pack()
        subWinLab10.pack()
        subWinLab02.pack()
        subWinLab03.pack()
        subWinLab04.pack()
        subWinLab09.pack()
        subWinLab05.pack()
        subWinLab06.pack()
        subWinLab07.pack()
        subWinLab08.pack()
        subWinLab12.pack()

    movieListBox.bind('<Double-Button-1>',movieInfo)
    recommendBtn.pack()

    win.mainloop()
