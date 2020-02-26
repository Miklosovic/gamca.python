import math
pi = math.pi
from random import randrange, randint

##1

##x = int(input("Prve cislo: "))
##y = int(input("Druhe cislo: "))
##vysledok = int(x/y)
##zvysok = x - int(vysledok) * y
##print (vysledok, "zvysok je ", zvysok)

##2

##x = int(input("Strana stvorca: "))
##obvod = x*4
##obsah = x**2
##print ("obvod je ", obvod, "obsah je ", obsah)

##3

##a = int(input("prva strana: "))
##b = int(input("druha strana: "))
##c = int(input("tretia strana: "))
##povrch = 2*(a*b + b*c + a*c)
##objem = a*b*c
##print ("povrch je ", povrch, "objem je ", objem)

##4

##r = float(input("polomer: "))
##obvod = 2*pi*r
##obsah = pi*(r**2)
##objem = (4/3)*pi*(r**3)
##print("obvod je ", obvod, "obsah je ", obsah, "objem je ", objem)

##5

##x = float(input("zadaj X: "))
##print ("tretia mocnina je ", x**3, "siesta mocnina je ", x**6)

##6

##x = float(input("zadaj vklad: "))
##y = float(input("zadaj rocny urok v percentach: "))
##print ("suma na konci roka je ", x + x*y/100)

##7

##h = int(input("pocet hodin: "))
##m = int(input("pocet minut: "))
##s = int(input("pocet sekund: "))
##print("v sekundach to je ", h*3600 + m*60 + s)

##8

##s = int(input("pocet sekund: "))
##hodiny = int(s/3600)
##minuty = int((s - hodiny*3600)/60)
##sekundy = int(s - hodiny*3600 - minuty*60)
##print (hodiny, "hodin", minuty, "minut", sekundy, "sekund")

##9

##S = int(input("suma: "))
##patsto = int(S/500)
##dvesto = int((S - patsto*500)/200)
##sto = int((S - patsto*500 - dvesto*200)/100)
##patdesiat = int((S - patsto*500 - dvesto*200 - sto*100)/50)
##dvadsat = int((S - patsto*500 - dvesto*200 - sto*100 - patdesiat*50)/20)
##desat = int((S - patsto*500 - dvesto*200 - sto*100 - patdesiat*50 - dvadsat*20)/10)
##pat = int((S - patsto*500 - dvesto*200 - sto*100 - patdesiat*50 - dvadsat*20 - desat*10)/5)
##print (patsto, " v 500€ , ", dvesto, " v 200€ , ", sto, " v 100€ , ", patdesiat, " v 50€ , ", dvadsat, " v 20€ , ", desat, " v 10€ , ", pat, " v 5€ , ")

##10

##s = float(input("spotrebu auta na 100 km: "))
##c = float(input("cena za 1l benzínu v €: "))
##v = float(input("vzdialenosť v km: "))
##vysledok = s*v*c/100
##print (round(vysledok,2), "€   stoji benzín potrebný na cestu")

##11

##x = float(input("X "))
##y = float(input("Y "))
##if x > y:
##    text = "X je vacsie ako Y"
##elif y > x:
##    text = "Y je vacsie ako X"
##else:
##    text = "X a Y sa rovnaju"
##print(text)

##12

##a = float(input("a = "))
##b = float(input("b = "))
##if a == 0:
##    text = "v rovnici ax + b = 0 s neznamou x neexistuje koren rovnice"
##    print (text)
##else:
##    text = "v rovnici ax + b = 0 s neznamou x je koren rovnice  "
##    x = -b/a
##    print (text, x)

##13

##x = float(input("x = "))
##y = float(input("y = "))
##z = float(input("z = "))
##if x > y and x > z:
##    print ("maximum je X")
##if y > x and y > z:
##    print ("maximum je Y")
##if z > y and z > x:
##    print ("maximum je Z")

##14 + 15

##x = float(input("x = "))
##y = float(input("y = "))
##z = float(input("z = "))
##if x <= 0 or y <= 0 or z <= 0:
##    print ("wait that's illegal")
##elif x + y > z and x + z > y and y + z > x:
##    if x == (y**2 + z**2)**(1/2) or y == (x**2 + z**2)**(1/2) or z == (x**2 + y**2)**(1/2):
##        print ("pravouhly")
##    elif x == y == z:
##        print("rovnostranny")
##    elif x == y or y == z or z == x:
##        print("rovnoramenny")
##    else:
##        print("random trojuholnik")
##else:
##    print ("nope")

##16

##m = float(input("hmotnost [kg]: "))
##h = float(input("vyska [m]: "))
##bmi = m/(h**2)
##if bmi < 18.5:
##    print("žer vác")
##elif bmi > 30:
##    print("jedz míň")
##else:
##    print("papkaj dalej")

##17

##a = int(input("a = "))
##if int(a/3) == float(a/3) and int(a/2) == float(a/2):
##    print("delitelne 6")
##elif int(a/3) == float(a/3):
##    print("delitelne 3")
##elif int(a/2) == float(a/2):
##    print("delitelne 2")
##else:
##    print("delitelne 1")

##18/19

##print("zoradenie cisel vzostupne")
##a = float(input("A = "))
##b = float(input("B = "))
##c = float(input("C = "))
##if a > b > c:
##    print("C B A")
##elif a > c > b:
##    print("B C A")
##elif b > a > c:
##    print("C A B")
##elif b > c > a:
##    print("A C B")
##elif c > a > b:
##    print("B A C")
##elif c > b > a:
##    print("A B C")
##else:
##    print("you broke the law")

##20

##a = float(input("A = "))
##b = float(input("B = "))
##c = float(input("C = "))
##if a == b == c:
##    print("mas 3 klony")
##elif a == b or b == c or c == a:
##        print("mas 2 klony")
##else:
##        print("mas 3 random cisla")

##21

##z = float(input("tvoje money: "))
##x = float(input("volny den: "))
##y = float(input("volna hodina: "))
##if x != 1 and y <= 17 and z >= 25:
##    print("chod do kina o 17. a divadla o 20.")
##elif x != 1 and y >= 17 and 18 > z >= 7:
##    print("ides do kina o 20.")
##elif x != 1 and y <= 17 and 25 > z >= 14:
##    print("ides do kina o 17. aj o 20.")
##elif x != 1 and 17 < y <= 20 and z >=18:
##    print("ides do divadla o 20.")
##elif x == 1 and y <= 17 and z >= 14:
##    print("ides do kina o 17. aj o 20.")
##elif x == 1 and y <= 17 and 14 > z >= 7:
##    print("ides do kina o 17. alebo 20.")
##elif x == 1 and 17 < y <= 20 and z >= 7:
##    print("ides do kina o 20.")
##else:
##    print("zostan doma")

##26

##p = 50
##x = 0
##for _ in range (p):
##    x += 2
##    print(x)

##28

##a = int(input("a = "))
##b = int(input("b = "))
##p = a - b
##d = 0
##y = 0
##for _ in range(p):
##    x = b + d 
##    if x/3 == int(x/3) and x <= a:
##        print(x)
##        y += x
##    else:
##        pass
##    d += 1
##print("sucet je  ", y)

##31

##n = float(input("n = "))
##k = float(input("k = "))
##print(n**k)

##33

##n = int(input("6-ciferne cislo =  "))
##for _ in range(6):
##    a = n%10
##    n = n//10
##    print(a)


##35

##x = int(input("veduci zvoli cislo od 2 po 9:  "))
##n = 0
##d = 1
##for _ in range(100):
##    n += d
##    if n%10 == x or (n//10)%10 == x or n/x == n//x:
##        print("*")
##    else:
##        print(n)

##37

##n = 0
##for i in range(1000):
##    x = i + 1
##    for j in range(i):
##        y = j + 1
##        if x//y == x/y:
##            n = n + y
##    if n == x:
##        print(x)
##    n = 0
    
##38

##n = int(input("cele cislo:  "))
##x = 1
##d_x = 0
##y = 0
##for _ in range(n):
##    x += d_x
##    d_x = 2
##    print(x)
##    y += x
##print("sucet je", y)


##41
    
##42

##x = int(input("x = "))
##y = int(input("y = "))
##a = x
##b = y
##if x > y:
##    for _ in range(y):
##        z = b 
##        if x//z == x/z and y//z == y/z:
##            print(z)
##        else:
##            pass
##        b -= 1
##else:
##    for _ in range(x):
##        z = a 
##        if x//z == x/z and y//z == y/z:
##            print(z)
##        else:
##            pass
##        a -= 1

##43

##44

##45

##n = int(input("n =  "))
##a = n
##d = 1
##b = 1
##while a >= 1:
##    a -= d
##    d += 1
##    if n%a == 0:
##        print(n, "nie je prvocislo")
##        a = 0
##        b = 0
##    else:
##        pass
##if b == 1:
##    print(n, "je prvocislo")
##else:
##    pass




