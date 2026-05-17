#A gyakorlás a Debreceni Egyetem (Dr. Varga Imre) python gyakorló feladatai alapjan történt

#megyunk tovabb a harmadik feladattal
#Írj egy Python programot, amely bekér egy dolgozat pontszámot (x) a felhasználótól és kiír egy érdemjegyet az alábbiak szerint! 1: x<50; 2: 50<=x<60; 3: 60<=x<70; 4: 70<=x<85; 5: x>=85.

dolgozat_pontszam_x = float(input("Írd meg, hány pontot/százalékot (%) értél el a dolgozatban: "))

if dolgozat_pontszam_x < 50:
    print("Az érdemjegyed: 1")
elif dolgozat_pontszam_x < 60:
    print("Az érdemjegyed: 2")
elif dolgozat_pontszam_x <  70:
    print("Az érdemjegyed: 3")
elif dolgozat_pontszam_x < 85:
    print("Az érdemjegyed: 4")
else:
    print("Az érdemjegyed: 5")