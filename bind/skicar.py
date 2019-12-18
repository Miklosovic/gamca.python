import tkinter
from random import randrange, randint

x_max, y_max = 800, 600

c = tkinter.Canvas(width = x_max, height = y_max, bg = "white")
c.pack()

r = 25
s, v = x_max, y_max

c.create_rectangle (s - 2*r, v - 2*r, s, v, fill="blue")
c.create_rectangle (s - 4*r, v - 2*r, s - 2*r, v, fill="red")
c.create_rectangle (s - 6*r, v - 2*r, s - 4*r, v, fill="green")
c.create_rectangle (s - 8*r, v - 2*r, s - 6*r, v, fill="yellow")

a, b = 0, y_max - 2*r

c.create_rectangle (a, b, a + 2*r, b + 2*r)
c.create_oval (a, b, a + 2*r, b + 2*r)
c.create

k = False
farba = "black"
hrubka = 1

def klik(event):
    global x_klik, y_klik
    global k
    global farba
    global hrubka
    x_klik, y_klik = event.x, event.y
    k = True

    if s > x_klik > s - 2*r and v > y_klik > v - 2*r :
        farba = "blue"
    elif s - 2*r > x_klik > s - 4*r and v > y_klik > v - 2*r :
        farba = "red"
    elif s - 4*r > x_klik > s - 6*r and v > y_klik > v - 2*r :
        farba = "green"
    elif s - 6*r > x_klik > s - 8*r and v > y_klik > v - 2*r :
        farba = "yellow"

    

def pusti(event):
    global k
    k = False


def kresli(event):
    global x_klik, y_klik
    x_kresli, y_kresli = event.x, event.y
    if k == True:
        c.create_line(x_klik, y_klik, x_kresli, y_kresli, fill=farba, width=hrubka)
        x_klik, y_klik = x_kresli, y_kresli
        

c.bind("<ButtonPress>", klik)   
c.bind("<ButtonRelease>", pusti)
c.bind("<Motion>", kresli)

tkinter.mainloop()
