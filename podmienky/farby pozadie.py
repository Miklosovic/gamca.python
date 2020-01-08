import tkinter
from random import randrange, randint

x_max, y_max = 1280, 720

c = tkinter.Canvas(width = x_max, height = y_max, bg = "white")
c.pack()

r_max, g_max, b_max = 255, 255, 255
r, g, b = randint(r_max), randint(g_max), randint(b_max)
d_r, d_g, d_b = 1, -1, 1
while True:
    farba =  f"#{r:02x}{g:02x}{b:02x}"
    c.create_rectangle (0,0,x_max,y_max, fill=farba, outline=farba)
    if r_max>r>0:
        r += d_r
    elif r == r_max or r == 0:
        d_r *= -1
    if g_max>g>0:
        g += d_g
    elif g == g_max or g == 0:
        d_g *= -1
    if b_max>b>0:
        b += d_b
    elif b == b_max or b == 0:
        d_b *= -1
    
    
           
    print (r,g,b)
    c.update()
    c.after(1)
    

