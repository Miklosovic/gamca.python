import tkinter
from random import randrange, randint

x_max, y_max = 800, 600

c = tkinter.Canvas(width = x_max, height = y_max, bg = "white")
c.pack()

r = 25
s, v = x_max, y_max
a, b = 0, y_max - 2*r
m, n = x_max - 2*r, 0

def vymaz():

    c.create_rectangle (s - 2*r, v - 2*r, s, v, fill="black")
    c.create_rectangle (s - 4*r, v - 2*r, s - 2*r, v, fill="red")
    c.create_rectangle (s - 6*r, v - 2*r, s - 4*r, v, fill="green")
    c.create_rectangle (s - 8*r, v - 2*r, s - 6*r, v, fill="blue")


    c.create_rectangle (a, b, a + 2*r, b + 2*r)
    c.create_oval (a+r - r/12, b+r - r/12, a+r + r/12, b+r + r/12, fill="black")

    c.create_rectangle (a + 2*r, b, a + 4*r, b + 2*r)
    c.create_oval (a+3*r - r/6, b+r - r/6, a+3*r + r/6, b+r + r/6, fill="black")

    c.create_rectangle (a + 4*r, b, a + 6*r, b + 2*r)
    c.create_oval (a+5*r - r/3, b+r - r/3, a+5*r + r/3, b+r + r/3, fill="black")


    c.create_rectangle (m, n, m + r, n +r)

vymaz()

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
        farba = "black"
    elif s - 2*r > x_klik > s - 4*r and v > y_klik > v - 2*r :
        farba = "red"
    elif s - 4*r > x_klik > s - 6*r and v > y_klik > v - 2*r :
        farba = "green"
    elif s - 6*r > x_klik > s - 8*r and v > y_klik > v - 2*r :
        farba = "blue"

    if a < x_klik < a + 2*r and b < y_klik < y_max:
        hrubka = 1
    elif a + 2*r < x_klik < a + 4*r and b < y_klik < y_max:
        hrubka = 3
    elif a + 4*r < x_klik < a + 6*r and b < y_klik < y_max:
        hrubka = 5

    

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
