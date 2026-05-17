#A gyakorlás a Debreceni Egyetem (Dr. Varga Imre) python gyakorló feladatai alapjan történt

#6. feladat

#Írj egy Python programot, amely bekér három egész számot a felhasználótól és kiírja a képernyőre, hogy mind a három páros szám-e (igen/nem)!

bekert_szam1 = int(input("Írj be egy tetszöleges egész számot: "))
bekert_szam2 = int(input("Írj be még egy tetszöleges egész számot: "))
bekert_szam3 = int(input("Írj be megint egy tetszöleges egész számot: "))

if bekert_szam1 % 2 == 0:
    if bekert_szam2 % 2 == 0:
        if bekert_szam3 % 2 == 0:
            print("Igen, mind a három szám páros")
else:
    print("Nem mind a három szám páros")
