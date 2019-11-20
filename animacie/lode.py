import tkinter
import random
canvas=tkinter.Canvas(height=600, width=800, bg="white")
canvas.pack()


def vlajka (x,f):
    canvas.create_oval(x,270,x+250,470, fill="brown")
    canvas.create_line(x+125,270,x+125,170)
    canvas.create_rectangle (x+125,70,x+275,170, fill=f)

def mesiac(x,y,r,s,F,f):
    canvas.create_oval (x-r,300+y-r,x+r,300+y+r, fill=F, outline=F)
    canvas.create_oval (x-r+s,300+y-r,x+r+s,300+y+r, fill=f, outline=f)
    return "moon"

def mesiac_opak (x,y,r,s,F,f):
    canvas.create_oval (x-r+s,300+y-r,x+r+s,300+y+r, fill=f, outline=f)
    canvas.create_oval (x-r,300+y-r,x+r,300+y+r, fill=F, outline=F)

def lod (x,y,s,v):
    canvas.create_polygon (x,y,x+(800-s)/8,y+2*v/11,x+3*(800-s)/8,y+2*v/11,x+4*(800-s)/8,y, fill="brown", outline="black")
    canvas.create_rectangle (x+9*(800-s)/40,y,x+11*(800-s)/40,y-4*v/11, fill="brown")
    canvas.create_polygon (x+11*(800-s)/40,y-2*v/11,x+3*(800-s)/8,y-16*v/55,x+11*(800-s)/40,y-4*v/11, fill="green", outline="black")
    mesiac_opak(x+11*(800-s)/80,y-275,v/22,v/22,"brown","white")
    mesiac(x+5*(800-s)/16,y-275,v/22,v/22,"white","brown")


a, x, y=150, 120, 100

for _ in range (1000):
    canvas.delete("all")
    #uloha 2

    vlajka(0,"green")

    #uloha 3

    vlajka(500,"red")

    canvas.create_rectangle(1,300,800,600, fill="blue")

    #uloha 1

    #uloha 4

    mesiac(200,-180,20,20,"red","green")
    
    #uloha 5

    mesiac(700,-180,20,20,"light blue","red")
    mesiac_opak(650,-180,20,20,"red","light blue")

    #uloha 6

    b=280
  
    lod(a,b,400,300)
    a+=3
    
    b+=70
   
    lod(x,b,400,300)
    x+=8

    b+=100
           
    lod(y,b,400,300)
    y+=10       

    #uloha animacia
    
    canvas.update()
    canvas.after(20)
   





    
