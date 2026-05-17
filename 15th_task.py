#A gyakorlás a Debreceni Egyetem (Dr. Varga Imre) python gyakorló feladatai alapjan történt

#15.feladat


# Írj egy Python eljárást, amely paraméterként kap egy egész számot és
# kiírja a képernyőre az ennél kisebb értékű elemeit a Fibonacci sornak!

#FYI: a Fibonacci sor a elözö számok összege, például: 0,1,1,2,3,5 stb.

bekert_egesz_szam = int(input("Adj meg egy egész számot: "))

a = 0
b = 1

def fibonacci_kisebb(k):
    global a, b
    while a < k: #azert az a valtozo, es nem a b, mert mindig 0-tól (kisebbtöl) indítjuk
        print(a, end="")
        a, b = b, a+b

fibonacci_kisebb(bekert_egesz_szam)

if __name__ == "__main__":
    fibonacci_kisebb(bekert_egesz_szam)

