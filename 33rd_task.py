#A gyakorlás a Debreceni Egyetem (Dr. Varga Imre) python gyakorló feladatai alapjan történt

#33.feladat

#Írj egy Python programot, amely egy tetszőleges méretű listában tárolt számok mediánját határozza meg! 
# (Ne importáld a statistics csmagot!)

random_lista = [4, 11, 15, 7, 21, 19, 25, 29, 35, 21, 15, 41, 17]

#mivel a medianhoz novekvö sorrendbe kell állítani
random_lista.sort()

#a median szamolasahoz paratlan szamu lista eseten egy egesz szamot kapunk, paros esetben a ket kozepso tag atlaga
if len(random_lista) % 2 ==1:
    median = random_lista[(len(random_lista) // 2)] #floor-divison, megnezzuk hanyszor van meg, maradékot figyelmen kivul hagyva
else:
    median = (random_lista[len(random_lista) // 2-1] + random_lista[(len(random_lista) // 2)])/2

print(median)
