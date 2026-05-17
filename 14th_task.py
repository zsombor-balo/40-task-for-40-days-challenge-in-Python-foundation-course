#A gyakorlás a Debreceni Egyetem (Dr. Varga Imre) python gyakorló feladatai alapjan történt

#14.feladat

#Írj egy Python eljárást, amely paraméterként kap 2 egész számot (N és M) és kiír a 
# képernyőre a csillag (*) karaktereket M darab sorban és N darab oszlopban 
# (tehát NxM darab karaktert egy téglalap alakú képernyőrészre)! 
# A programodban hívd is meg ezt az alprogramot!

bekert_szamN = int(input("Adj meg egy számot: "))
bekert_szamM = int(input("Adj meg még egy számot: "))

def csillagrajz(N,M):
    for i in range(M):
        print("*" * N)

if __name__ == "__main__":
    csillagrajz(bekert_szamN, bekert_szamM)