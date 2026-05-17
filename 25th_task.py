#A gyakorlás a Debreceni Egyetem (Dr. Varga Imre) python gyakorló feladatai alapjan történt

#25.feladat

#Ìrj egy Python programot, amely a felhasználótól pozitív számokat kér be mindaddig, amíg 
# a felhasználó nullát nem ad be! A program az összes értéket tárolja egy listában, majd írja ki a képernyőre a lista elemeit 
# fordított sorrendben!

pozitiv_szamok = [] #listába taroljuk

while True:
    szam = int(input("Adj meg egy számot (egy idö után 0-t adj meg): "))
    if szam == 0:
        break
    elif szam > 0:
        pozitiv_szamok.append(szam)
    else:
        print("Invalid Input! Adj meg egy pozitív egész számokat!")

Lforditott_szamok = pozitiv_szamok[::-1]
print(Lforditott_szamok)