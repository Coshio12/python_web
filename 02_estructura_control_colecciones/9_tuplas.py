"""
    Las tuplas son consideradas como una lista, pero una caracteristica diferente
    Los datos de las tuplas son inmutables, no se pueden modificar
"""
#Creamos una tupla
tupla = ('Ale',25,1.78)

#Podemos acceder a los datos como una lista normal y con indices
A= tupla[0]
#Devuelve el primer valor de la lista
print(A)

#Devuelve el ultimo valor de la lista
B = tupla[-1]
print(B)

#Tambien podemos usar el slicing para sacar un conjunto de datos de la tupla
C = tupla[:1]
print(C)

#Con el metodo len podemos sacar el tamaño de la tupla
D = len(tupla)
print(D)

#Con el metodo index podemos saber en que posicion esta un valor
E = tupla.index(25)
print(E)

#Si tratamos de usar el metodo append, pop, remove
#Devolvera un error
