import tkinter
import random
X_MAX, Y_MAX = 800, 600
canvas = tkinter.Canvas(width=X_MAX, height=Y_MAX)
canvas.pack()

def farba():
    r=random.randrange(256)
    g=random.randrange(256)
    b=random.randrange(256)
    return f"#{r:02x}{g:02x}{b:02x}"

def vlak(x,y,r,d,f):
    canvas.create_rectangle(x-r-r/5,y+d/5,x+r+r/5,y+2*d/5, fill="black")
    canvas.create_rectangle(x-r,y-d,x+r,y+d, fill=f)
    canvas.create_oval(x-7*r/8,y+3*d/5,x-r/8,y+7*d/5, fill="black")
    canvas.create_oval(x+7*r/8,y+3*d/5,x+r/8,y+7*d/5, fill="black")

x=200
y=100
r=80
d=50
for _ in range(3):
    a=random.randint(1,3)
    for _ in range(a):
        vlak(x,y,r,d,farba())
        x+=2*r+2*r/5
    x=200
    y+=200       
