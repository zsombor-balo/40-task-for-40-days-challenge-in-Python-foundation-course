#A gyakorlás a Debreceni Egyetem (Dr. Varga Imre) python gyakorló feladatai alapjan történt

#10.feladat kovetkezik

#Írj egy Python programot, amely bekér egy pozitív egész számot a felhasználótól és kiírja aképernyőre azt a számot, amely az ennél a számnál nem nagyobb pozitív egész számok összege!

bekert_szam = int(input("Adj meg egy pozitív egész számot: "))

eredmenyosszeg = 0 #mivel mindig 0-rol indulunk 

if bekert_szam >= 0:
    for i in range(bekert_szam + 1):
        eredmenyosszeg += i
    print("A pozitív egész számok összege, amelyek nem nagyobbak, az általad megadott számnál: ", eredmenyosszeg)