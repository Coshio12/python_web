"""
    La instruccion del es una palabra reservada que sirve para quitar elementos
    de diferentes tipos de datos, como ser listas, diccionarios
    Incluso puede borrar la declaracion de alguna variable
    Es un metodo diferente a pop
"""
#Definimos una lista
A = ['a','b','c','d']

#Usamos la instruccion del pasandole la variable y la posicion
#Para eliminar el valor en dicha posicion
del A[1]
print(A)

#Volvemos a declarar la variable
A = ['a','b','c','d']
#Podemos usar slicing para eliminar mas de un valor de la lista
del A[:3]
print(A)

#tambien podemos dejar la variable totalmente vacia
del A[:]
print(A)

#Podemos usar esta instruccion con un diccionario
#Creamos un diccionario
d = {'uno': 1, 'dos': 2}
#Para poder eliminar colocamos del le pasamos la variable y dentro del corchete la clave deseada
del d['dos']
print(d)

#Y si solo colocamos la variable del diccionario
#Elimina la declaracion de la variable dando asi un error
del d
print(d)
