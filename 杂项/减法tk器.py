from tkinter import *

tk = Tk()
frame = Frame(tk)
frame.pack(padx=10, pady=10)

v1 = StringVar()
v2 = StringVar()
v3 = StringVar()

def test(d):
    return d.isdigit()

    
cut = tk.register(test)

e1 = Entry(frame, width=10, textvariable=v1, validate="key",validatecommand=(cut, '%P')).grid(row=0,column=0)

Label(frame, text='-').grid(row=0,column=1)

e2 = Entry(frame, width=10, textvariable=v2, validate="key",validatecommand=(cut, '%P')).grid(row=0,column=2)

Label(frame, text='=').grid(row=0,column=3)

e3 = Entry(frame, width=10, textvariable=v3, state='readonly').grid(row=0,column=4)

def cut_num():
    i = int(v1.get()) - int(v2.get())
    v3.set(i)


Button(frame, text='结果', command=cut_num).grid(row=1, column=2,pady=2)

mainloop()
