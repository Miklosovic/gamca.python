import tkinter
from random import randint, randrange
x_max, y_max = 800, 800
c=tkinter.Canvas(width = x_max, height = y_max, bg = "black")
c.pack()

for _ in range(10000):
    r = 5
    x, y = randint(r, x_max-r), randint(r, y_max-r)
    if (2*x_max/7<=x<=3*x_max/7):
        farba = "blue"
    elif (3*y_max/7<=y<=4*y_max/7):
        farba = "blue"
    else:
        farba = "white"

    c.create_oval (x-r,y-r,x+r,y+r, fill=farba, outline=farba)
    #c.after(1)
    #c.update()
    
