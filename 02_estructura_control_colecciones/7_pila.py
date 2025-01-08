"""
    En este archivo veremos que es una pila
    Pila se usa con variables del tipo lista
    Siguiendo la logica la ultima en entrar la primera en irse
    Para poder simular una pila usaremos los metodos que ya vimos con anterioridad
    En este caso el pop y el append
"""
#Definimos la variable pila
pila = [1,2,3]

#Con el metodo append agregamos dos valores
pila.append(4)
pila.append(5)

#Despues usamos el metodo pop para eliminar el ultimo valor de la lista
#En este caso el numero 5
pila.pop()

#Mostramos el resultado
print(pila)

#Volvemos a usar el pop y ahora se eliminara el numero 4
pila.pop()

#Mostramos el resultado
print(pila)
#De esa manera podemos simular una pila con los metodos aprendidos
