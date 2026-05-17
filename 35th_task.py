#A gyakorlás a Debreceni Egyetem (Dr. Varga Imre) python gyakorló feladatai alapjan történt

#35.feladat

#Írj egy Python függvényt, amely paraméterként kap egy szót (sztringet) és megmondja, hogy ez egy palindróm-e! 
# A programodban hívd is meg ezt az alprogramot!

#a polindrom olyan szó, mely balról és jobbról is olvasva ugyanaz
def palindroma(szo):
    return szo[::-1]

eredmeny = palindroma("icipici")

if eredmeny == "icipici":
    print("igen, ez egy palindróma")
else:
    print("nem palindróma")

