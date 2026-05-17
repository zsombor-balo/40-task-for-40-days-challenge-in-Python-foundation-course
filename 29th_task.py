#A gyakorlás a Debreceni Egyetem (Dr. Varga Imre) python gyakorló feladatai alapjan történt

#29.feladat

#Írj egy Python programot, amely megmondja előfordul-e (igen/nem) a Debrecen szó a temp.txt fájlban!

#elöször set-up-oljuk a metódust ami beolvassa a fájlt (a fájt viszont nincs letöltve directory-ba igy ccsak sablonnak jó)
tartalom = open('temp.txt', 'r') #sima beolvasás (r)


if "Debrecen" in tartalom:
    print("igen")
else:
    print("nem")