#A gyakorlás a Debreceni Egyetem (Dr. Varga Imre) python gyakorló feladatai alapjan történt

#13.feladat

# Írj egy Python programot, amely bekér két pozitív egész számot a felhasználótól 
# és kiírja a képernyőre azokat a páros számokat, amelyek a két adott érték 
# közötti zárt intervallumban találhatóak!

bekert_pozitiv_szam1 = int(input("Adj meg egy pozitív egész számot: "))
bekert_pozitiv_szam2 = int(input("Adj meg még egy pozitív egész számot: "))

for i in range(bekert_pozitiv_szam1, bekert_pozitiv_szam2+1):
    if i % 2 == 0:
        print(i)