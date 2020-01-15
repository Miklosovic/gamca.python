import math
pi = math.pi

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

s = int(input("pocet sekund: "))
hodiny = int(s/3600)
minuty = int((s - hodiny*60)/60)
sekundy = int(s - hodiny*3600 - minuty*60)
print (hodiny, "hodin", minuty, "minut", sekundy, "sekund")

