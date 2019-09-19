from tkinter import *

tk = Tk()

ass = Scale(tk, from_=0, to=500)
ass.pack()
sea = Scale(tk,from_=0, to=200, orient=HORIZONTAL)
sea.pack()

def get():
    print(ass.get(),sea.get())

Button(tk, text='获取位置', command=get).pack()

mainloop()


