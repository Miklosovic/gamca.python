import tkinter
import random
canvas=tkinter.Canvas(height=600, width=800, bg="white")
canvas.pack()

#uloha 2

def vlajka (x,f):
    canvas.create_oval(x,270,x+250,470, fill="brown")
    canvas.create_line(x+125,270,x+125,170)
    canvas.create_rectangle (x+125,70,x+275,170, fill=f)

vlajka(0,"green")

#uloha 3

vlajka(500,"red")

canvas.create_rectangle(1,300,800,600, fill="blue")

#uloha 1

Y=random.randrange(100,200)
def mesiac(x,y,r,s,F,f):
    canvas.create_oval (x-r,300+y-r,x+r,300+y+r, fill=F, outline=F)
    canvas.create_oval (x-r+s,300+y-r,x+r+s,300+y+r, fill=f, outline=f)

mesiac(450,Y,40,40,"yellow","blue")
mesiac(450,-Y,40,40,"yellow","white")

#uloha 4

mesiac(200,-180,20,20,"red","green")

#uloha 5

def mesiac_opak (x,y,r,s,F,f):
    canvas.create_oval (x-r+s,300+y-r,x+r+s,300+y+r, fill=f, outline=f)
    canvas.create_oval (x-r,300+y-r,x+r,300+y+r, fill=F, outline=F)

mesiac(730,-180,20,20,"light blue","red")
mesiac_opak(650,-180,20,20,"red","light blue")







