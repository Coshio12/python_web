"""
    los diccionarios son aquellos que pueden guardar varios datos como una lista o una tupla
    pero lo guarda de una manera en especial, con clave y valor
    Se los conoce como los arreglos asosiativos en otros lenguajes
    Donde estas claves y valores pueden ser tanto enteros como del tipo string
"""
#Definimos un diccionario con llaves
numeros= {
    'uno': 1,
    'dos': 2,
    'tres': 3,
    'cuatro': 4,
    'cinco': 5
}
#Mostramos como se ve la variable en la consola
print(numeros)

#Podemos acceder a la informacion del diccionario segun la clave/key
A= numeros['uno']
#Mostramos el resultado
print(A)

#Para agregar un dato, debemos llamar primero a la variable, añadir la nueva clave y con un igual
#Su nuevo vaalor
numeros['seis'] = 6
#Mostramos el resultado
print(numeros)

#Para poder buscar algun dato dentro del diccionario se hace con su clave
#Y si es necesario se añade un mensaje si no se encuentra dicho dato
B= numeros.get('cuatro','No se encontro')
#Mostramos el resultado
print(B)

#Si solo necesitamos las claves del direccionario
#Podemos usar el metodo keys() el cual solamente devolvera las claves
C = numeros.keys()
#Mostramos el resultado
print(C)

#Si solo queremos los valores del diccionario
#Podemos usar el metodo values() el cual solamente devolvera los valores
D = numeros.values()
#Mostramos el resultado
print(D)

#Si necesitamos tanto clave como valor podemos usar el metodo items()
#Pero seria lo mismo que usar la variable del diccionario
E = numeros.items()
#Mostramos el resultado
print(E)

#Para poder eliminar un valor del diccionario
#Usamos el metodo pop y que reciba como primer parametro una clave del diccionario
#Y si es necesario como segundo parametro un mensaje de no encontrado
numeros.pop('seis','No se encontro')
#Mostramos el resultado
print(numeros)

#El metodo clear borra todos los datos del diccionario
numeros.clear()
#Mostramos el resultado
print(numeros)

#Volvemos a declarar la variable del diccionario
numeros= {
    'uno': 1,
    'dos': 2,
    'tres': 3,
    'cuatro': 4,
    'cinco': 5
}

#Podemos realizar operaciones iterativas con los bucles
#En estos ejemplos usaremos el bucle for
#Este bucle for devolvera las solamente las claves del diccionario
for numero in numeros:
    print(numero)

#Este for devolvera los valores del diccionario con el metodo values
for numero in numeros.values():
    print(numero)

#Este bucle for devolvera tanto la clave con el valor con el metodo items
for clave, valor in numeros.items(): #Dentro de un bucle for podemos declarar varias variables
    print(clave, valor)
