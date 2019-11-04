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

def vlak():
    for i in range(2,5):
        canvas.create_rectangle(x-r-r/5,y-9*d/10,x+r+r/5,y-8*d/10, fill="black")
        canvas.create_rectangle(x-r,y-d,x+r,y+d, fill=farba)
        canvas.create_oval()
        
