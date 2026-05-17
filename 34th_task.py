#A gyakorlás a Debreceni Egyetem (Dr. Varga Imre) python gyakorló feladatai alapjan történt

#34.feladat

#Írj egy Python programot, amely a temp.txt szöveges fájl minden második szavát
# (szóközzel elválasztott részsztringjét) a képernyőre írja!

with open("temp.txt", 'r') as fajl:
    tartalom = fajl.read()
    szavak = tartalom.split() # tartalmat felbonjukt szorol szora, ami ezt egy listaban tarolja el
    for i in range(1, len(szavak) ,2): #minedn masodik
        print(szavak[i])

