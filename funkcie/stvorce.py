import tkinter
import random
X_MAX, Y_MAX = 800, 600
canvas=tkinter.Canvas(width=X_MAX, height=Y_MAX)
canvas.pack()

def stvorce(x,y,r,p,s):
    for i in range(p):
        canvas.create_rectangle(x+r,y+r,x-r,y-r)
        r-=s

for j in range(100):
    stvorce(random.randint(150,650),random.randint(150,450),random.randint(75,150),random.randint(5,10),random.randint(2,10))
