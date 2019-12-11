import tkinter
from random import randrange, randint
x_max, y_max = 800, 600
c=tkinter.Canvas(width = x_max, height = y_max)
c.pack()

for _ in range(1000):

    x, y = randint(-50,50), randint(-50,50)

    if (x+x_max/2<=x_max/2) and (y+y_max/2<=y_max/2):
        farba = "red"
    elif (x+x_max/2>=x_max/2) and (y+y_max/2<=y_max/2):
        farba = "green"
    elif (x+x_max/2>=x_max/2) and (y+y_max/2>=y_max/2):
        farba = "yellow"
    elif (x+x_max/2<=x_max/2) and (y+y_max/2>=y_max/2):
        farba = "blue"

    c.create_line(x_max/2, y_max/2, x_max/2+x, y_max/2+y, fill=farba, width=2)
