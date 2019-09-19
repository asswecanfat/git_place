from tkinter import *

ass = Tk()

frame = Frame(ass)

photo = PhotoImage(file='tex3.png')
thelable = Label(frame, image=photo)
thelable.pack()

thebutton1 = Button(frame,image=photo,text='左奶子', fg='yellow', compound=CENTER)
thebutton1.pack(side=LEFT, padx=100, pady=50)

thebutton2 = Button(frame, image=photo, text='右奶子', fg='blue', compound=CENTER)
thebutton2.pack(side=RIGHT,padx=100, pady=50)

frame.pack(padx=10,pady=10)

mainloop()
