from tkinter import *
from textblob import *

win = Tk()

win.title("spelling checker")
win.geometry("700x400")
win.config(background="#dae6f6")
def spellcheck():
    word = txt.get()
    a = TextBlob(word)
    right = str(a.correct())

    cs = Label(win,text="correct text is : ",font=("trebuchet ms",20),bg="#dae6f6",fg="#364971")
    cs.place(x = 100 , y = 250)

    spell.config(text=right)


lb = Label(win,text="spelling checker",font=("Trbuchet MS",20),bg="#dae6f6",fg="#364971")
lb.pack()

txt = Entry(win,justify="center",width=30,font=("poppins",25),bg="white",border=2)
txt.pack(pady=10)
txt.focus()

butt = Button(win,text="check",font=("arial",20,"bold"),fg="white",bg="red",command=spellcheck)
butt.pack()

spell = Label(win,font=("poppins",20),bg="#bae6f6",fg="#364971")
spell.place(x = 350 , y = 250)
win.mainloop()