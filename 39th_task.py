#A gyakorlás a Debreceni Egyetem (Dr. Varga Imre) python gyakorló feladatai alapjan történt

#39.feladat

#Írj egy Python programot, amely a teknőcgrafika és eseményvezérlés segítségével billentyűnyomás 
# hatására egy szabályos poligont rajzol ki! A ’3’-as karakter esetén háromszöget, a ’4’-es hatására négyszöget, 
# és így tovább egészen a szabályos kilencszögig. Mindegyik sokszög legyen más színű!

import turtle

teknos = turtle.Turtle()

#eloszor a haromszög

def haromszog():
    teknos.begin_fill()
    teknos.color("blue")
    for i in range(2):
        teknos.forward(100)
        teknos.left(135)
    teknos.end_fill()


#most jojjen a 4szog
def negyszog():
    teknos.color("red")
    teknos.begin_fill()
    for i in range(4):
        teknos.forward(100)
        teknos.left(90)
    teknos.end_fill()

#most jöjjön az ötszög
def otszog():
    teknos.color("yellow")
    teknos.begin_fill()
    for i in range(5):
        teknos.forward(100)
        teknos.left(70)
    teknos.end_fill()

#6szög kovetkezik
def hatszog():
    teknos.color("black")
    teknos.begin_fill()
    for i in range(6):
        teknos.forward(100)
        teknos.left(60)
    teknos.end_fill()

#hétszög (belso szogek 128 fok korul)
def hetszog():
    teknos.color("green")
    teknos.begin_fill()
    for i in range(7):
        teknos.forward(100)
        teknos.left(52) #180-128 fok
    teknos.end_fill()

#nyolcszög következik
def nyolcszog():
    teknos.color("grey")
    teknos.begin_fill()
    for i in range(8):
        teknos.forward(100)
        teknos.left(45) #180-135 fok (belso szogek 135fok)
    teknos.end_fill()

#kilencszög következik
def kilencszog():
    teknos.color("orange")
    teknos.begin_fill()
    for i in range(9):
        teknos.forward(100)
        teknos.left(40) #180-140 fok (belso szogek 140fok)
    teknos.end_fill()

#tetszes szerint lehet futtatni
# haromszog()
# negyszog()
# otszog()
# hatszog()
# hetszog()
# nyolcszog()
kilencszog()

turtle.done()