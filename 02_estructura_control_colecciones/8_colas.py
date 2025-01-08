"""
    Logramos simular una pila: el ultimo en entrar es el primero en salir
    Ahora vamos a simular una coa, que es el primero en entrar es el primero en salir
"""
#Para ello vamos a tener que importar una de las librerias de python
#Que se llama deque de collections
from collections import deque #Esta es una de las sintaxis para importar una libreria
#Tambien se puede de las siguiente manera:
#import collections
#Pero importaria toda la informacion de collections

#Declaramos una lista usando uno de los metodos que importamos
cola = deque(['Alejandro','Samir','Luis'])
print(type(cola))
#Con esta linea vemos que no es una lista comun, sino del tipo de la libreria importada

#Agregamos un valor a la lista ya creada con el metodo append
cola.append('Daniela')

#Devolvemos el resultado
print(cola)

#Ahora para poder simular una cola usamos un metodo de la libreria importada
cola.popleft()

#Mostramos el resultado
print(cola)

#Y de esta manera podemos simular una cola
