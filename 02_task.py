#A gyakorlás a Debreceni Egyetem (Dr. Varga Imre) python gyakorló feladatai alapjan történt
# napi 1 feladat 40 napon keresztul

#Írj egy Python programot, amely bekér három számot a felhasználótól és kiírja a képernyőre, hogy három különböző értéket kapott-e!

bekert_szam1 = int(input("Adj meg egy számot: "))
bekert_szam2 = int(input("Adj meg még egy számot: "))
bekert_szam3 = int(input("Adj meg megint egy utolsó számot: "))

if bekert_szam1 != bekert_szam2 and bekert_szam1 != bekert_szam3 and bekert_szam2 != bekert_szam3:
    print("Három kulönbozö szamot adttál meg!")
else:
    print("Nem adtál meg három kulönbozö szamot!")
