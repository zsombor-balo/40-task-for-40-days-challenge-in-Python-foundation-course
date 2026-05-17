#A gyakorlás a Debreceni Egyetem (Dr. Varga Imre) python gyakorló feladatai alapjan történt

#12.feladat

#Írj egy Python programot, amely először bekér egy kisebb majd egy nagyobb pozitív valós számot 
# a felhasználótól és kiírja a képernyőre azokat az egész számokat, 
# amelyek a megadott értékek között helyezkednek el!

bekert_szam1 = float(input("Adj meg légyi egy számot!"))
bekert_szam2 = float(input("Adj meg egy elözönél nagyobb számot!"))


for i in range(int(bekert_szam1)+1, int(bekert_szam2)):
    if i > bekert_szam1 and i < bekert_szam2:
        print(int(i))
    else:
        print("A megadott két szám közötti tartományban nincs egész szám!")
