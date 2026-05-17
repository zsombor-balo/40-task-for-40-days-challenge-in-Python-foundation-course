#A gyakorlás a Debreceni Egyetem (Dr. Varga Imre) python gyakorló feladatai alapjan történt

#31.feladat

# Írj egy Python programot, amely bekér egy dátumot három pozitív egész számként (év, hó, nap)! 
# A program határozza meg, hogy az adott dátum az év hányadik napja!

nap = int(input("Adj meg egy számot (nap): "))
honap = int(input("Adj meg egy számot (hónap): "))
ev = int(input("Adj meg egy számot (év): "))

#kezeljuk a paros honapokat, Aprilis,Junius stb (februar szokoev miatt kesobb kezeljuk)
paros_honapok = [4, 6, 9, 11]

#ugyanezt a paratlanoknal (Januar, Marcius stb)
paratlan_honapok = [1, 3, 5, 7, 8, 10, 12]

#a napok szamlalasahoz letrehozunk egy szamlalot
napok_szam = 0

for i in range(1, honap):
    if i in paratlan_honapok:
        napok_szam += 31 #ezek a paratlan honapok, tehat Januar, MArcius, ezert 31 mert annyi nap van
    elif i in paros_honapok:
        napok_szam += 30
    elif i == 2:
        if (ev % 4 == 0 and ev % 100 != 0) or (ev % 400 == 0 ):
            napok_szam += 29
        else:
            napok_szam += 28

napok_szam += nap

print(f" A bekêrt datum az ev {napok_szam}. napja")