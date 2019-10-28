import tkinter
import random
canvas=tkinter.Canvas(height=600,width=800,bg="white")
canvas.pack()

def strom (x,y,r):
    canvas.create_rectangle(x-10,y+10,x+10,y+110, fill="brown", outline="brown")
    canvas.create_oval (x+r,y+r,x-r,y-r, fill="green", outline="green")


def trava (x,y,s,v):
    for _ in range (3,10):
        canvas.create_line(x,y,s,v, fill="green", width=random.randint(1,2))       
        v-=random.randrange(3,7)
        s+=random.randrange(3,10)
for _ in range (20):
    x=random.randrange(1,800)
    y=random.randrange(1,600)
    trava (x,y,x+random.randrange(-25,25),y-random.randrange(0,5))
for _ in range (10):
    x=random.randrange(1,800)
    y=random.randrange(1,600)
    strom (x,y,random.randint(10,50))

