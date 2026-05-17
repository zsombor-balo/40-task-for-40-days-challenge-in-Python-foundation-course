#A gyakorlás a Debreceni Egyetem (Dr. Varga Imre) python gyakorló feladatai alapjan történt

#18.feladat

#Írj egy Python függvényt, amely paraméterként kap 2 egész számot és visszatér a két szám által meghatározott 
# zárt intervallumban található egész számok összegével! 
# A programodban hívd is meg ezt az alprogramot!

bekert_szam1 = int(input("Adj meg egy számot: "))
bekert_szam2 = int(input("Adj meg még egy számot: "))

def intervallum_osszeg(szam1, szam2):
    if szam1 > szam2:
        szam1, szam2 = szam2, szam1 # egy sorban cseréljük fel, máskülönben egymás alá írva, az also felulirna felsöt, és nem jó a végeredmény (order of operations miatt)
    return sum(range(szam1, szam2+1))

eredmeny = intervallum_osszeg(bekert_szam1, bekert_szam2)

print(eredmeny)
