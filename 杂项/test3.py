from tkinter import *

tk = Tk()
sb = Scrollbar(tk)
sb.pack(side=LEFT, fill=Y)

the = Listbox(tk, yscrollcommand=sb.set)
the.pack(side=LEFT, fill=BOTH)

for i in range(1500):
    the.insert(END, str(i))
sb.config(command=the.yview)
theButton = Button(tk, text='删除', command=lambda x=the:x.delete(ACTIVE))
theButton.pack()

mainloop()
