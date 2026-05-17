#A gyakorlás a Debreceni Egyetem (Dr. Varga Imre) python gyakorló feladatai alapjan történt

#Írj egy Python programot, amely bekér egy egész számot a felhasználótól és kiírja a 
# képernyőre, hogy osztható-e (igen/nem) a szám 3-mal vagy 5-tel! 

bekert_szam = int(input("Írj be egy tetszöleges számot: "))

if bekert_szam % 3 == 0:
    print("A szám, amit megadtál osztható 3-mal.")
elif bekert_szam % 5 == 0:
    print("A szám, amit megadtál osztható 5-el.")
else:
    print("A szám amit megadtál nem osztható sem 3-mal, sem pedig 5-el")
