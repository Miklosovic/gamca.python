import tkinter
from random import randrange, randint 
#r, g, b = 255, 255, 255
#color = f"#{r:02x}{g:02x}{b:02x}"
x_max, y_max = 800, 600
c=tkinter.Canvas(width = x_max, height = y_max, bg = "white")
c.pack()

d = 20
x, y = randint(d, x_max-d), randint(d, y_max-d)
farba = "white"
dx, dy = 3, 3
dc = -1


while True:
    c.delete("all")
    r, g, b = 255, 255, 255
    color = f"#{r:02x}{g:02x}{b:02x}"
    c.create_text(x,y, text="RIP", font="Arial 15")

    y += dy
    x += dx
    
    if y>= y_max - d or y <= d:
        dy *= -1 
    if (x <= d or x >= x_max - d):
        dx *= -1

    print (r)
    c.update()
    c.after(1)

        
