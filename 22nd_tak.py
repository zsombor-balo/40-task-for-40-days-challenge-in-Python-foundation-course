#A gyakorlás a Debreceni Egyetem (Dr. Varga Imre) python gyakorló feladatai alapjan történt

#22.feladat

#  Írj egy Python eljárást, amely paraméterként kap egy pozitív egész számot és kiír a képernyőre ennyi karaktert úgy, 
# hogy minden harmadik karakter pluszjel (+) legyen a többi viszont mínuszjel (-)! 
# A programodban hívd is meg ezt az alprogramot!

def plusz_minusz(a):
    for i in range(1, a+1):
        if i % 3 == 0:
            print("+", end=" ") # csak egy sima empty space (whitespace) teszünk, hogy jobban lassuk a karakterekt
        else:
            print("-", end=" ")

plusz_minusz(7)

#itt kicsit komolyabb a meghívás
if __name__ == "__main__":
    plusz_minusz(16)

