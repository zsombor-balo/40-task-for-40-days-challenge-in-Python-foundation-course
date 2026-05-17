#A gyakorlás a Debreceni Egyetem (Dr. Varga Imre) python gyakorló feladatai alapjan történt

#11.feladat

#Írj egy Python programot, amely bekér egy pozitív egész számot a felhasználótól 
# és kiírja a képernyőre felváltva a 0 és 1 számjegyeket úgy, hogy a számjegyek együttes d
# arabszáma pontosan a megadott szám legyen!

bekert_szam = int(input("Írj be egy pozitív egész számot: "))
if bekert_szam > 0 :
    for i in range(bekert_szam):
        if i % 2 == 0:
            print(0, end="")
        else:
            print(1, end="")
else:
    print("Invalid input!Érvényes számot adj meg")

