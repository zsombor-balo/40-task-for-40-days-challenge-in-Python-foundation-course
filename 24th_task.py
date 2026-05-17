#A gyakorlás a Debreceni Egyetem (Dr. Varga Imre) python gyakorló feladatai alapjan történt

#24.feladat


#Írj egy Python programot, amely bekér a felhasználótól egy mondatot (sztringet) és 
# ezt úgy íratja ki, hogy a szóköz karaktereket kihagyja!

mondat = input("Adj meg egy mondatot: ")
szavak = mondat.split() 
print("A bekért mondat így hangzik szóköz (space) nélkül: ", "".join(szavak))