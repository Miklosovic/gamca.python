import tkinter
from random import randrange, randint

x_max, y_max = 800, 600

c = tkinter.Canvas(width = x_max, height = y_max, bg = "white")
c.pack()

r = 50
s, v = x_max, y_max
a, b = 0, y_max - r
m, n = x_max - r, 0

def vymaz():

    #farba

    c.create_rectangle (s - r, v - r, s, v, fill="black")
    c.create_rectangle (s - 2*r, v - r, s - r, v, fill="red")
    c.create_rectangle (s - 3*r, v - r, s - 2*r, v, fill="green")
    c.create_rectangle (s - 4*r, v - r, s - 3*r, v, fill="blue")

    #hrubka

    c.create_rectangle (a, b, a + r, b + r)
    c.create_oval (a + r/2 - r/24, b + r/2 - r/24, a + r/2 + r/24, b + r/2 + r/24, fill="black")

    c.create_rectangle (a + r, b, a + 2*r, b + r)
    c.create_oval (a+3*r/2 - r/12, b + r/2 - r/12, a+3*r/2 + r/12, b + r/2 + r/12, fill="black")

    c.create_rectangle (a + 2*r, b, a + 3*r, b + r)
    c.create_oval (a+5*r/2 - r/6, b + r/2 - r/6, a+5*r/2 + r/6, b + r/2 + r/6, fill="black")

    #vymaz

    c.create_rectangle (m, n, m + r, n +r)
    c.create_text (m + r/2, n + r/2, text = "VYMAZ", font = "Arial 10")

vymaz()

k = 0
farba = "black"
hrubka = 1

def klik(event):
    global x_klik, y_klik
    global k
    global farba
    global hrubka
    x_klik, y_klik = event.x, event.y
    k = 1

    if s > x_klik > s - r and v > y_klik > v - r :
        farba = "black"
    elif s - r > x_klik > s - 2*r and v > y_klik > v - r :
        farba = "red"
    elif s - 2*r > x_klik > s - 3*r and v > y_klik > v - r :
        farba = "green"
    elif s - 3*r > x_klik > s - 4*r and v > y_klik > v - r :
        farba = "blue"

    if a < x_klik < a + r and b < y_klik < y_max:
        hrubka = 1
    elif a + r < x_klik < a + 2*r and b < y_klik < y_max:
        hrubka = 3
    elif a + 2*r < x_klik < a + 3*r and b < y_klik < y_max:
        hrubka = 5

    if m < x_klik < x_max and n < y_klik < n + r:
        c.delete("all")
        vymaz()
        c.update()

    
def pusti(event):
    global k
    k = 0


def kresli(event):
    global x_klik, y_klik
    x_kresli, y_kresli = event.x, event.y
    if k == 1:
        c.create_line(x_klik, y_klik, x_kresli, y_kresli, fill=farba, width=hrubka)
        x_klik, y_klik = x_kresli, y_kresli
        

c.bind("<ButtonPress>", klik)   
c.bind("<ButtonRelease>", pusti)
c.bind("<Motion>", kresli)

tkinter.mainloop()
