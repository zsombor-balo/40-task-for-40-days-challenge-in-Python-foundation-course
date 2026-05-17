#A gyakorlás a Debreceni Egyetem (Dr. Varga Imre) python gyakorló feladatai alapjan történt

#Írj egy Python programot, amely bekér egy pozitív egész számot a felhasználótól 
#és kiírja a képernyőre azokat a pozitív hárommal osztható számokat, amelyek kisebbek az adott számnál!

bekert_szam = int(input("Írj be egy pozitív egész számot: "))

if bekert_szam > 0 :
    for i in range(1, bekert_szam):
        if i  % 3 == 0:
            print("A pozitiv harommal osztható szamok, melyek kisebbek a megadott szamnál:", i)
else: 
    print("Invalid Input!")





#ez mar nem resze a feladtnak, de a vegeredmeny szebb
#listaba rendezzuk , mivel a for ciklus kiprinteli minden egyes szamot egymas alá kulon sorba
lista = []
if bekert_szam > 0 :
    for i in range(1, bekert_szam):
        if i  % 3 == 0:
            lista.append(i)
    print("A pozitiv harommal osztható szamok, melyek kisebbek a megadott szamnál:",lista)
else: 
    print("Invalid Input!")


