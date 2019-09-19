from tkinter import *

root = Tk()

Label(root, text = '作者:').grid(row = 0, column = 0)
Label(root, text = '作品:').grid(row = 1, column = 0)

e1 = Entry(root)
e2 = Entry(root)
e1.grid(row = 0, column = 1, sticky=W,padx=10, pady=10)
e2.grid(row = 1, column = 1, sticky=W,padx=10, pady=10)

def show():
    print('作者：' + e1.get() + '\n' + '作品：' + e2.get())

Button(root, text = '展示', command=show).grid(row = 2, column = 0, sticky=W, padx=10, pady=10)
Button(root, text = '退出', command=root.quit).grid(row = 2, column = 1, sticky=E, padx=10, pady=10)

mainloop()
