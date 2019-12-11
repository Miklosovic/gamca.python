import tkinter
from random import randint, randrange
x_max, y_max = 800, 800
c=tkinter.Canvas(width = x_max, height = y_max, bg = "black")
c.pack()

for _ in range(10000):
    r = 10
    x, y = randint(r, x_max-r), randint(r, y_max-r)
    if (2*x_max/5<=x<=3*x_max/5 and y_max/5<=y<=4*y_max/5):
        farba = "white"
    elif (x_max/5<=x<=4*x_max/5 and 2*y_max/5<=y<=3*y_max/5):
        farba = "white"
    else:
        farba = "red"

    c.create_oval (x-r,y-r,x+r,y+r, fill=farba, outline=farba)
    c.after(1)
    c.update()
    
