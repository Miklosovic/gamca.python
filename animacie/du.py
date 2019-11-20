import tkinter
import random
c=tkinter.Canvas(width=800, height=600)
c.pack()

while True:
    x, y, r, p=random.randrange(770), random.randrange(570), 10, 1000
    t= c.create_oval(x-r,y-r,x+r,y+r, fill="light blue")
    c.move(t, random.randrange(-15,15), random.randrange(5,15))
    c.update()
    c.after(20)
         

