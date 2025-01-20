"""
    Dentro de una aplciacion es posible tener mas de dos errores
    Para ello try except es de gran ayuda para generar con exactitud el mensaje indicado
    ya sea para el programador o para el usuario
"""
#Creamos una aplicacion donde el usuario da  dos numeros un dividendo y un divisor
#Aqui hay dos errores que pueden pasar
#1. Que no se digite el tipo de dato necesario para que funcione el programa
#2. Que sea una division entre cero

#Creamos la variable que guarda el resultado
divi = 0
#Iniciamos el try
try:
    #Le pedimos al usuario dos valores
    a = int(input('Ingrese el Dividendo: '))
    b = int(input('Ingrese el Divisor: '))

    #Realizamos la operacion
    divi = a / b
#Usamos el primero except y tenemos que heredar de la clase padre Exception y le damos un alias
except Exception as error:
    #Imprimimos el mensaje, y el error lo colocamos en un type y llamamos al name de la clase de donde esta error
    print('Ha ocurrido este error: ',type(error).__name__)

#Al digitar un valor normal y divirlo entre cero la clase se llama ZeroDivisionError entonces
#Si se llama a este error le personalizamos un mensaje por si se da este error
except ZeroDivisionError:
    print('Error: No se puede dividir entre cero')

#Al digitar un valor que no sea un numero entero muestra la clase ValueError entonces
#Si se llama a este error le personalizamos un mensaje por si se da este error
except ValueError:
    print('Error: Solo se permiten numeros enteros')


print('La division es: ', divi)

#De esta manera manejamos los errores
