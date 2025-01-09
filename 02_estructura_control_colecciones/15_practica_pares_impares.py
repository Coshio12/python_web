"""
    Aplicando lo aprendido en esta seccion, intenta resolver el siguiente problema
    antes de ver el codigo final
    
    GUARDAR RESULTADOS DE PARES E IMPARES
    Crea 2 listas y una tupla que tendra numeros de 1 a 9. La primera lista se llamara
    pares y el segundo impar, ambos estaran vacios
    Despues multiplica cada uno de los numeros de la tupla por un numero aleatorio entre 1 y 100
    Si el resultado es par guarda ese numero en la lista de pares y si es impar en la lista de impares.
    Muestra por consola la multiplicacion que se produce junto con su resultado con el formato 2 x 3 = 6
    Y la lista de pares e impares
"""
print('='*40)
print('GUARDANDO RESULTADOS DE PARES E IMPARES')
print('='*40)
#Importamos la libreria de random
import random

#Creando las listas y la tupla
pares = []
impares = []
tupla = (1,2,3,4,5,6,7,8,9)

print('Variables iniciales')
print('='*40)
print('Lista de pares: ', pares)
print('Lista de impares: ', impares)
print('Tupla: ', tupla)
print('='*40)

#Variable extra
texto = ''

print('PRODUCTO DE LOS NUMEROS ALEATORIOS')
print('='*40)
for numero in tupla:
    valor_random = random.randint(1,100) #guardando un valor random entre 1 y 100
    multiplicacion = numero * valor_random #multiplicando los valores de la tupla por un numero random entre 1 y 100
    
    if multiplicacion % 2 == 0: #condicion para saber si es par o impar
        pares.append(multiplicacion)
        texto = 'PAR'
    else:
        impares.append(multiplicacion)
        texto = 'IMPAR'
    #Cumpliendo la condicion de mostrar en consola la operacion entre el valor de la tupla y un numero aleatorio entre 1 y 100
    print(f'Producto: {numero} x {valor_random} = {multiplicacion} es {texto}')

#Mostrando los resultados de una manera mas ordenada
print('='*40)
print('---------------RESULTADOS---------------')
print('='*40)
print('Lista final con los pares guardados')
print(pares)
print('='*40)
print('Lista final con los impares guardados')
print(impares)
print('='*40)

