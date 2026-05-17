#A gyakorlás a Debreceni Egyetem (Dr. Varga Imre) python gyakorló feladatai alapjan történt

#19.feladat

# Írj egy Python programot, amely bekér két szót (sztringet) a felhasználótól 
# és kiírja a képernyőre, hogy van-e olyan betű, amelyik mind a kettőben előfordul!

szo1 = input("Adj meg egy szót: ")
szo2 = input("Adj meg még egy szót: ")


van_kozos_betu = False #eloszor false-ra allitjuk ,azzal kezdjuk es idokozben atvalt True-ra ha van benne

for betu in szo1:
    if betu in szo2:
        van_kozos_betu = True
        break

if van_kozos_betu:
    print("Van közös betü a két szóban")
else:
    print("Nincs közös szó a két szóban")