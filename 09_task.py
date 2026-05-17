#A gyakorlás a Debreceni Egyetem (Dr. Varga Imre) python gyakorló feladatai alapjan történt

#9.feladat kovetkezik

#Írj egy Python programot, amely bekér egy 20-nál nem nagyobb pozitív egész számot a felhasználótól 
#és kiírja a képernyőre a START szót úgy, hogy előtte annyi szóköz legyen amennyi a megadott szám értéke!

bekert_szam = int(input("Írj be egy 20-nál nem nagyobb pozitív egész számot: "))

if  bekert_szam <= 20:
    print(" " * (bekert_szam) + "START")
else:
    print("Invalid Input! Próbáld újra!") 
