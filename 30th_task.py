#A gyakorlás a Debreceni Egyetem (Dr. Varga Imre) python gyakorló feladatai alapjan történt

#30.feladat

#Írj egy Python programot, amely a szamok.txt fájlba írja a 100 legkisebb 3-mal osztható pozitív egész számot!

#ugyanaz a metodus mint elobb, csak a w-t (write-írást) használjuk 
szamok_text = open('szamok.txt', 'w')

for i in range(1, 300+1):
    if i % 3 == 0:
        szamok_text.write(str(i) + "\n") #uj sorban kezdjuk es beleirjuk