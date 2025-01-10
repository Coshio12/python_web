"""
    Las funciones son formas de poder reutilizar el codigo en diferentes puntos de la aplicacion
    Normalmente se suelen usar para no tener que estar creando la misma operacion todo el tiempo
    Se usa la palabra reservada "def" despues el nombre de la funcion seguida de parentesis
    Y con una sangria debajo de esa linea, pueden ir todas las operaciones necesarias
    
    Puede recibir parametro o no
    Para que una funcion se active hay que llamar a la funcion
    Para ello en una nueva linea se debe colocar el nombre de la funcion seguida de parentesis
"""
global nombre

#Se define la funcion salidar
def saludar():
    print('Hola desde la funcion saludar')

#Se llamaa a la funcion
saludar()

#Tambien se le puede pasar una variable para poder utilizar dentro de la funcion
#Creamos una variable
nombre = 'Jose Cossio'

#Creamos otra funcion
def saludar_2():
    print('Hola desde la funcion 2')
    print(nombre)

#Llamamos a la funcion
saludar_2()

#Si dentro de la funcion se crea una variable
#Dicha variable solo servirara para operar dentro de la funcion no para operaciones fuera de la funcion
def saludar_3():
    nombre_2 = 'Jose'
    print('Hola desde saludar 3 ', nombre_2)
#Llamamos a la funcion y veremos que si detecta el nombre
saludar_3() 
#pero si tratamos de imprimiirlo por fuera devolvera un error
#Descomenta el siguiente print si quieres ver el error
#print(nombre_2) 

#Para solucionar el problema anterior lo que podemos hacer crear una variable global
#Para ello usaremos la palabra reservada global
def saludar_4():
    global nombre_apellido
    nombre_apellido = 'Jose Cossio'
    print('Hola desde saludar-4: ',nombre_apellido)

saludar_4()
print('La variable global esta aqui: ',nombre_apellido)
#Con la variable global permitara usar una variable en cualquier parte de la aplicacion
