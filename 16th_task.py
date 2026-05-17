#A gyakorlás a Debreceni Egyetem (Dr. Varga Imre) python gyakorló feladatai alapjan történt

#16.feladat


#Írj egy logikai értékkel visszatérő Python függvényt, amely paraméterként kap egy egész számot és 
# eldönti a számról, hogy osztható-e 2-vel és 3-mal is egyszerre! 
# A programodban hívd is meg ezt az alprogramot!

bekert_egesz_szam = int(input("Adj meg egy pozitív egész számot: "))

def oszthato(n):
    '''logikai értékkel visszatérö függvény'''
    if n % 2 == 0 and n % 3 ==0:
        return True
    else: 
        return False

#vizulaizáljuk is a képernyön
if oszthato(bekert_egesz_szam):
    print("A szám osztható 2-vel ês 3-mal is")
else:
    print("Nem osztható 2-vel és 3-mal egyszerre")