"""
    En esta seccion trabajaremos sobre los errores y como un sistema puede aceptar errores, para ello veremos
    varios tipos de errores
    Errores de sintaxis:
    Es aquel error que devuelve en la consola si algun metodo o variable se escribe de mala manera
    y cuando lo ejecutamos nos mostrara un main error
    
    Un main error, es aquel que muestra especificamente en que linea esta el error y que cual es el error
    Ahora te mostrare un error comun
"""
#Por ejemplo este es un error de sintaxis que no esta cumpliendo con la forma correcta de crear una clase
#Si descomentamos estas dos lineas y ejecutamos nos dara un error de sintaxis
# clas Persona():
#     pass

#pero si lo escribimos asi:
class Persona():
    pass
#Esta cumpliendo la sintaxis
#lo mismo pasa con metoodos o creacion de variables
#crearemos una variable sin cumplir la sintaxis y un metodo mal aplicado
#n
#Nos devuelve el siguiente error, donde nos muestra el archivo que tiene un error
#nos muestra la linea donde esta el error
#y tambien la razon del error
# Traceback (most recent call last):
#   File "c:\Users\Cosio\Workspace\python_web\06_errores_archivos\01_errores.py", line 22, in <module>
#     n
# NameError: name 'n' is not defined
#Para ello hay que resperar la sintaxis
n = 'Siguiendo la sintaxis'

#Lo mismo pasa si llamamos de manera erronea a un metodo
#prit()
#El error que devuelve
# Traceback (most recent call last):
#   File "c:\Users\Cosio\Workspace\python_web\06_errores_archivos\01_errores.py", line 32, in <module>
#     prit()
#     ^^^^
# NameError: name 'prit' is not defined. Did you mean: 'print'?

print(n)

#ERRORES EN TIEMPO DE EJECUCION (EXCEPCIONES)
#Estos errores se dan cuando estamos ejecutando un archivo

#Por ejemplo creamos una lista vacia
lista = []
#y si descomentamos la siguiente linea que esta tratando devolver el valor de una posicion sale error
#pero el entorno de desarrollo nos deja escribirlo, eso es un error de ejecucion
#lista[0] # IndexError: list index out of range

#Lo mismo pasaria si tratamos de eliminar un valor de lista
#lista.pop() #IndexError: pop from empty list

#O si tratamos de sumar un int con un str
#n = 10 + '10' #TypeError: unsupported operand type(s) for +: 'int' and 'str'
#n

#O si tratamos de convertir letras en numeros
#a = int(input()) #ValueError: invalid literal for int() with base 10: 'asd'

#Esos son diferentes errores de ejecucion donde el entorno de desarrollo no detecta error pero al ejecutar si hay un error

#GESTIONAR ERRORES
#Tomaremos un error y usaremos ciertas partes del mensaje para que aparezca en nuestro codigo
#Para ello creamos una aplicacion simple de sumar varios numeros

#Creamos el contador
contador = 0
#Creamos una variable donde se guardara el resultado de la suma
suma = 0
#Creamos un bucle hasta que se agreguen 3 numeros
while contador < 3:
    #Si usamos este codigo y comentamos lo que no esta comentado
    #Vemos una aplicacion simple que suma 3 numeros
    #Pero que pasa si en vez de colocar un numero colocamos una letra
    #Esta devolvera error y dejara de funcionar el codigo para ello gestionaremos ese error
    # n = int(input(f'Ingrese un numero {contador+1}:'))
    # suma += n
    # contador +=1
    
    #Para ello usaremos try y except donde try es donde se ejecutara el codigo con normalidad
    #Y el except se ejecutara si hay un error
    try:
        n = int(input(f'Ingrese un numero {contador+1}:'))
        suma += n
        contador +=1
    #En este caso como solo se aceptan numeros enteros nuestro mensaje debe decir:
    except:
        print('Error: Ingrese numeros enteros')
        #Esto permitira mostrar el mensaje y pedir otra vez el numero
    #Tambien el try except se le puede concatenar el else
    #Este se ejecutara despues de una vuelta del bucle imprimiendo el mensaje
    else:
        print('Todo ha funcionado correctamente')
    #Y finally solamente cuando se haya terminado la ejecucion de todo el programa
    finally:
        print('Fin de la ejecucion')

print(f'La suma total es: ', suma)
