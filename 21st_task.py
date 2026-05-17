#A gyakorlás a Debreceni Egyetem (Dr. Varga Imre) python gyakorló feladatai alapjan történt

#21.feladat

#Írj egy Python eljárást, amely paraméterként kap egy szót (sztringet) 
# és annyi darab csillag (*) karaktert ír ki a képernyőre, ahány karaktert tartalmazott a szó! 
# A programodban hívd is meg ezt az alprogramot!

bekert_szo = input("Adj meg egy szót: ")

def szo_csillag(szo):
    for betu in szo:
        print("*", end="")
    
szo_csillag(bekert_szo)