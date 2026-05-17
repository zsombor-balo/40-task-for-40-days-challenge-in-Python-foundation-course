#A gyakorlás a Debreceni Egyetem (Dr. Varga Imre) python gyakorló feladatai alapjan történt

#23.feladat

#Írj egy Python programot, amely bekér a felhasználótól egy mondatot (sztringet) 
# és ennek szavait (szóközzel elválasztott részsztringjeit) fordított sorrendben kiírja a képernyőre!

mondat = input("Adj meg egy mondatot: ")
szavak = mondat.split() # a split() metódussal felbonjuk a mondatokat, igy listba tudjuk majd tenni 
forditott_szavak = szavak[::-1]

# a listat ugy iratjuk ki, hogy mondat legyen belole (string concatenation), van tobb módja, most a join()-t hasznalom
print("A bekért mondat visszafelé kiírva a következö: ", " ".join(forditott_szavak))

