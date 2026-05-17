#A gyakorlás a Debreceni Egyetem python gyakorló feladatai alapjan történt, napi 1 feladat 40 napon keresztul
#kezdjuk az elso feladattal


#1. Írj egy Python programot, amely bekér három számot a felhasználótól és kiírja a képernyőre a legkisebb értéket ezek közül!

#bekerrunk harom szamot a felhasznalototl
elsoszam = int(input("Legyszi adj meg egy szamot: "))
masodikszam = int(input("Legyszi adj meg még egy szamot: "))
harmadikszam = int(input("Legyszi adj meg megint egy szamot: "))

#gyorsba meghatarozzuk a legkisebb szamot a harom kozul
if elsoszam < masodikszam and elsoszam < harmadikszam:
    legkisebb_szam = elsoszam
elif masodikszam < elsoszam and masodikszam < harmadikszam:
    legkisebb_szam = masodikszam
else:
    legkisebb_szam = harmadikszam

print(" A legkisebb szam amit valaszottal: ", legkisebb_szam)
