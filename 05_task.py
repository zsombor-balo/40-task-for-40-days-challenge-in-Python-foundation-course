#A gyakorlás a Debreceni Egyetem (Dr. Varga Imre) python gyakorló feladatai alapjan történt

#Írj egy Python programot, amely bekér három számot a felhasználótól és kiírja a képernyőre, hogy
#a számok közül bármelyik kettőnek az összege egyenlő-e a harmadik számmal!

bekert_szam1 = int(input("Írj be egy tetszöleges számot: "))
bekert_szam2 = int(input("Írj be egy tetszöleges számot megint: "))
bekert_szam3 = int(input("Írj be egy tetszöleges számot ismét: "))

if bekert_szam1 + bekert_szam2 == bekert_szam3:
    print("A számok közül, amit megadtál, az elsö kettönek az összege egyenlö a harmadik számmal.")
elif bekert_szam1 + bekert_szam3 == bekert_szam2:
    print("A számok közül, amit megadtál, az elsö és a harmadik szám összege egyenlö a második számmal.")
elif bekert_szam3 + bekert_szam2 == bekert_szam1:
    print("A számok közül, amit megadtál, a harmadik és a második szám összege egyenlö az elsö számmal.")
else:
    print("A számok közül amit megadtál, egyik kettönek az összege sem egyenlö a harmadik számmal.")
