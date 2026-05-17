#A gyakorlás a Debreceni Egyetem (Dr. Varga Imre) python gyakorló feladatai alapjan történt

#40.feladat

#Írj egy Python eljárást, amely paraméterként kap egy szavakból álló sztringet és kiírja ezeket a szavakat úgy, hogy a szavakon belül a betűk sorrendje fordított, de a szavak sorrendje az eredeti!

def forditott_sorrend_szavak(mondat):
    szavak = mondat.split()
    forditott_szavak = (szo[::-1] for szo in szavak)
    print(" ".join(forditott_szavak))


proba = "Szeretem az aljas, lebúj kurvákat"
forditott_sorrend_szavak(proba)
