import tkinter
from random import randint, randrange
x_max, y_max = 800, 800
c=tkinter.Canvas(width = x_max, height = y_max, bg = "black")
c.pack()

def pohyb(event):
    r = 8
    x,y = event.x, event.y
    c.create_oval (x-r,y-r,x+r,y+r, fill = "blue")
    a = x_max - x
    c.create_oval (a-r,y-r,a+r,y+r, fill = "orange")

c.bind("<Motion>", pohyb)
    
