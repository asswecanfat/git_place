from tkinter import *

tk = Tk()

frame1 = Frame(tk)#聊天框
frame2 = Frame(tk)#输入框
frame3 = Frame(tk)#图片框
frame4 = Frame(tk)#按钮框

frame1.grid(row=0, column=0, padx=20,pady=50)
frame2.grid(row=1, column=0,padx=20,pady=10)
frame3.grid(row=0, column=1,padx=10,pady=50)
frame4.grid(row=2, column=0,padx=10,pady=10)

v1 = StringVar()
#先聊天框
e1 = Entry(frame1, textvariable=v1, width=20).pack()







mainloop()
