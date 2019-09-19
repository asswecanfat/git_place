from tkinter import *
import math as m

tk = Tk()
w = Canvas(tk, width=600, height = 600)
w.pack()

center_x = 300
center_y = 300

point =[
    #A点
    center_x,
    center_y - 100,
    #B点
    center_x - int(100*m.cos(m.pi/6)),
    center_y + 50,
    #C点
    center_x + int(100*m.cos(m.pi/6)),
    center_y + 50,
    #A点
    center_x,
    center_y - 100
    ]

w.create_polygon(point, outline='red', fill='')

mainloop()
