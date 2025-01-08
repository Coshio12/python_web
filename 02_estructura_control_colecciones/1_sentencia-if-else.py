#La sentencia if
#Es una palabra reservada "if" que se encarga de realizar una operacion si se cumple una condicion

#Esta es la siguiente sintaxis
a = True
if a:
    print('Se cumple la condicion')
#Cuando un if se cumple o devuelve un True como respuesta correcta se ejecuta lo que esta en la siguiente linea
#de codigo siempre y cuando este con una sangria

#Cuando devuelve un False, no ejecuta nada, realiza la comparacion pero no ejecuta la accion indicada
b = False
if b:
    print('Se cumple la condicion')

#Pero al usar la para reservada "else" primero detecta que es false y salta a la siguiente operacion que tiene el else
#Realizando una operacion
if b:
    print("Se cumplio")
else:
    print('No se cumplio')
    
#Ejemplo practico
#Detectando si un numero es par o impar
#Para este caso debemos pedir un numero al usuario
#Volverlo entero y realizar la operacion que si el residuo entre 2 es igual a 0 nos devuelve que el numero
#Es par y si no lo es devuelva que es impar
n = int(input('Ingresa un numero entero: '))

if n % 2 == 0:
    print(f'El numero: {n} es PAR')
else: 
    print(f'El numero: {n} es IMPAR')
#Usando condiciones anidadas
#Vimos que las condiciones anidadas son una forma de expresar en el codigo restricciones para ejecutar diferentes acciones
#Es la mejor manera para poder realizar diferentes aplicaciones
#Ejemplo
n = int(input('Ingresa un numero entero: ')) #Pedimo el numero

if n != 0: #Si el numero es distinto de 0 avanzara al siguiente if
    if n > 0: #Si el numero mayor a 0 seguira al siguiente if
        if n % 2 == 0: #Si el residuo del numero entre 2 es igual a 0, devolvera PAR POSITIVO
            print(f'El numero {n} es PAR POSITIVO')
        else: #Si el residuo del numero entre 2 no es 0, devolvera IMPAR POSITIVO
            print(f'El numero {n} es IMPAR POSITIVO')
    else: # Si el numero es menor a 0 seguira al siguiente if
        if n % 2 == 0: #Si el residuo del numero entre 2 es igual a 0, devolvera PAR NEGATIVO
            print(f'El numero {n} es PAR NEGATIVO')
        else: #Si el residuo del numero entre 2 no es 0, devolvera IMPAR NEGATIVO
            print(f'El numero {n} es IMPAR NEGATIVO')
else: #Si el numero es 0, devolvera el mensaje de este else
    print(f'El numero {n} es NEUTRO')
