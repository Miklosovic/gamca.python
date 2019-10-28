import tkinter
import random
canvas=tkinter.Canvas(height=800, width=800)
canvas.pack()

def panelak(x,y,v,s):
    
    canvas.create_rectangle(x,y,x+20*s-10,y+20*v-10)
       
    for _ in range (1,s):
        p=y 
        for _ in range(1,v):
            canvas.create_rectangle(x+10,y+10,x+20,y+20)
            y+=20
        x+=20
        
def mesto():
    for _ in range(1,10):
        x=random.randrange(10,770)
        y=random.randrange(10,770)
        v=random.randrange(3,10)
        s=random.randrange(2,8)
        panelak(x,y,v,s)
mesto()
