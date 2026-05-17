#A gyakorlás a Debreceni Egyetem (Dr. Varga Imre) python gyakorló feladatai alapjan történt

#27.feladat

#Írj egy Python programot, amelyben megadsz egy tetszőleges egészeket tartalmazó listát, 
# majd elemeit csökkenő sorrendbe rendezed anélkül, hogy használnád a sort() metódust.

lista = [11,7,8,3,6,1,13,52,9,19,26,31]
for i in range(len(lista)):
    for k in range(i, len(lista)):
        if lista[i] < lista[k]:
            lista[i], lista[k] = lista[k], lista[i]
print(lista)


