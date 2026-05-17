#A gyakorlás a Debreceni Egyetem (Dr. Varga Imre) python gyakorló feladatai alapjan történt

#36.feladat

#36. Írj egy Python programot, amely a teknőcgrafika segítségével egy ötágú sárga csillagot rajzol ki!
#ehez a turtle könyvtárat kell használjuk azzal tudjuk megrajzolni
import turtle

#inicializaljuk
teknos = turtle.Turtle()
teknos.color("yellow")
teknos.begin_fill()
for i in range(5):
    teknos.forward(100)
    teknos.right(144)
teknos.end_fill()

turtle.done()