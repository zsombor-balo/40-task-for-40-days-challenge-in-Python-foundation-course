#A gyakorlás a Debreceni Egyetem (Dr. Varga Imre) python gyakorló feladatai alapjan történt

#8.feladat kovetkezik

#Írj egy Python programot, amely bekér egy valós (A) és egy egész (K) számot a felhasználótól és 
# kiírja a képernyőre az AK hatvány értékét anélkül, hogy használnád a ** operátort!

bekert_valos_szam_A = float(input("Írj be egy valós számot: "))
bekert_egesz_szam_K = int(input("Írj be egy egész számot: "))

#random eredmenyvaltozo, amivel inditunk (de eloszor validaljuk, hogy egyaltalan jo input erkezett-e be)
if bekert_egesz_szam_K > 0:
    eredmeny = 1
    for i in range(bekert_egesz_szam_K):
        eredmeny *= bekert_valos_szam_A
    print("Az AK hatvány értéke:", eredmeny)
else:
    print("Invalid Input! Próbáld újra")

