#A gyakorlás a Debreceni Egyetem (Dr. Varga Imre) python gyakorló feladatai alapjan történt

#37.feladat

#37. Írj egy Python programot, amely a teknőcgrafika segítségével kirajzol egy „házikó” alakú ötszöget!
import turtle

# /\
# | |
# __
#ehez hasonlot kell, tehat nem egy sima pentagramm

teknos = turtle.Turtle()
teknos.color("blue")

#eloszor az alap
teknos.begin_fill()
for i in range(4):
    teknos.forward(100)
    teknos.right(90)
teknos.end_fill()

#most jon a tetö haromszög, legyen a tetö szine piros
teknos.color("red")
teknos.begin_fill()
teknos.left(45)
teknos.forward(75)
teknos.right(95)
teknos.forward(70)
teknos.end_fill()

#indítjuk a jatekot
turtle.done()