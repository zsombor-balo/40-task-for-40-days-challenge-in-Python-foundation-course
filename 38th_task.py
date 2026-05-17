#A gyakorlás a Debreceni Egyetem (Dr. Varga Imre) python gyakorló feladatai alapjan történt

#38.feladat

#Írj egy Python programot, amely a teknőcgrafika segítségével kirajzol egy 30, 40 és 50 egység 
# oldalhosszúságú derékszögű háromszöget!
import turtle 

teknos = turtle.Turtle()
teknos.color("blue")

# derekszogu haromszognel a pitagorsz tetellel kiszamolva a szogek nagyysaga es felkerekitve
# teknos.forward(30)
# teknos.left(126.87) #53.13 fokos szog
# teknos.forward(50)
# teknos.left(143.13) #36.87 fokos szog
# teknos.forward(40)

#mivel eleg kicsik a 30, 40, 50 egyseg megtizszerezem, hogy jobban lathato legyen a keprenyon

teknos.forward(300)
teknos.left(126.87) #53.13 fokos szog
teknos.forward(500)
teknos.left(143.13) #36.87 fokos szog
teknos.forward(400)
turtle.done()