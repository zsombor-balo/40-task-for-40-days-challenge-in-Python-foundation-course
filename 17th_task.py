#A gyakorlás a Debreceni Egyetem (Dr. Varga Imre) python gyakorló feladatai alapjan történt

#17.feladat

#Írj egy logikai értékkel visszatérő Python függvényt, amely paraméterként kap három számot és eldönti, 
# hogy az összes paramétere pozitív-e! A programodban hívd is meg ezt az alprogramot!

szam1 = int(input("Adj meg egy számot: ")) 
szam2 = int(input("Adj meg megint egy számot: ")) 
szam3 = int(input("Adj meg még egy számot: ")) 

def osszes_pozitiv(a, b, c):
    if a >= 0:
        if b >= 0:
            if c >= 0:
                return True
    else:
        return False
    
if osszes_pozitiv(szam1, szam2, szam3):
    print("Igen, mind a 3 szám pozitív")
else:
    print("Valamelyik szám a 3 közül nem pozitív")