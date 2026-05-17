#A gyakorlás a Debreceni Egyetem (Dr. Varga Imre) python gyakorló feladatai alapjan történt

#28.feladat

# Írj egy Python programot, amely bekér egy pozitív egész számot (N) és létrehoz egy listát, 
# amely a Fibonacci sor legkisebb értékű N darab elemét tartalmazza! 
# Majd a program írja ki a lista páros értékű elemeit!

N_bekert_szam = int(input("Adj meg egy pozitív egész számot: "))

fibonacci_sor = [0, 1] #ezzel muszaj indítani a sort, így legalabb 3-at kell bekérni

while len(fibonacci_sor) < N_bekert_szam:
    kovetkezo_szam = fibonacci_sor[-1] + fibonacci_sor[-2]
    fibonacci_sor.append(kovetkezo_szam)

for szam in fibonacci_sor:
    if szam % 2 == 0:
        print(szam, end="")