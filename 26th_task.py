#A gyakorlás a Debreceni Egyetem (Dr. Varga Imre) python gyakorló feladatai alapjan történt

#26.feladat

#Írj egy Python programot, amelyben megadsz egy tetszőleges listát, majd a program létrehoz egy 
# másik listát, amelynek elemei megegyeznek az előbbi lista elemeivel ismétlődések nélkül

lista = [1,2,3,5,8,13,8,3]


masik_lista = set(lista) 

#mivel a set csak egy "unique" 'set'-eket hoz létre, így listava kell alakitani
masik_lista = list(masik_lista)
print(masik_lista)