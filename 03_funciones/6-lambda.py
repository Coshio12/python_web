"""
    Funciones lambda
    Es creada con la pabra reservada lambda, podemos usarla donde sea
    
    La funcion lambda sirve para crear funciones que realicen una sola operacion
    para poder retornar ya sea un valor en especifico o un valor boolean
    
"""
#En siguiente codigo muestra como estabamos creando una funcion de suma
#definiendo una funcion y recibiendo dos parametros
def suma(a,b):
    return a + b

#En cambio al usar la palabra reservada podemos crear la misma funcion suma
#De una manera mas directa y en una sola linea
#Siguiendo la sintaxis
#Primero la variable donde se guardara el resultado, luego la palabra reservada lambda
#despues los parametros que recibira, seguido de dos puntos y la operacion que se quiere realizar
sumar = lambda a,b: a+b
print(f'la suma es: {sumar(10,20)}')

#El siguiente codigo muestra una funcion anonima para duplicar un valor dado
doblar = lambda n: n*2
print(f'El doble del numero es: {doblar(10)}')

#El siguiente codigo nos devolvera un booleano True o False
#En este caso si el numero recibo divido 2 y su residuo es cero devolvera true si no devolvera false
par = lambda n: n%2 == 0
print(f'El numero es par? {par(10)}')

#En este caso si el numero recibo divido 2 y su residuo es diferente de cero devolvera true si no devolvera false
impar = lambda n: n%2 != 0
print(f'El numero es impar? {impar(12)}')

#Tambien puede recibir cadenas de texto
#En este caso con el slicing haremos que imprima la cadena de texto al reves
revertir = lambda cadena: cadena[::-1] #derecha a izquiera
print(f'La cadena de texto al reves es: {revertir('Alejandro')}')
