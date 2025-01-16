"""
    Despues de ver el funcionamiento de como nosotros como programadores 
    Mostramos la informacion por consola de nuestros archivos
    Existen diferentes proyectos antiguos que muestran la informacion de distinta manera
    Asi que en este archivo te mostrare las diferentes formas de formatear la informacion
"""
#Para eso usaremos la logica del archivo anterior de entra-script
#Importamos desde sys solamente el metodo argv
from sys import argv

#Usaremos uno de sus metodos que es argv que segun los valores que se le pasan
#mueve todo a una lista
#Este if verifica que la lista sea de tamaño4  para poder ejecutarse si no es asi, devolvera un mensaje de error
if len(argv) == 4:
    #Esta variable con el metodo argv[1] detecta el texto que se le pasara
    #NOTA: El texto debe estar entre comillas ("") para que la consola detecte que es un texto
    nombre = argv[1]
    
    #Esta variable guarda el valor de un numero entero que debemos transformarlo
    edad = int(argv[2])
    #Esta variable guarda el valor de un numero float que debemos transformarlo
    altura = float(argv[3])

    #Usamos el print basico que aprendimos en las primeras lecciones
    print(f'Nombre: {nombre} \nEdad: {edad} \nAltura: {altura}') 
    #Dejando las llaves en medio, y usando el metodo format pasandole como argumentos las variables creadas
    #tenemos otra forma de mostrar los datos
    print('Nombre: {} \nEdad: {} \nAltura: {}'.format(nombre,edad,altura))
    #Tambien si entre las llaves colocamos el nombre de una variable y en format le asignamos el valor
    #tambien podemos mostrar la informacion
    print('Nombre: {n} \nEdad: {e} \nAltura: {a}'.format(a = altura, n = nombre, e = edad))
    #Y por ultimo usando el tipo de dato de las variables junto con el porcentaje podemos mostrar la informacion
    #s  = str, i ? int, f = float
    print('Nombre: %s \nEdad: %i \nAltura: %f'%(nombre,edad,altura))
    
    """
    Sobre estos ultimos puntos dejo la documentacion para ver los distintos valores 
    que se pueden colocar
        Formate de ahora y con format() y f

        https://docs.python.org/es/3/tutorial/inputoutput.html

        Antigua forma de formatear

        https://docs.python.org/es/3/library/stdtypes.html#old-string-formatting
    """
else:
    print('Error, ingresa los argumentos correctamente')
    print('Ejemplo: formateo.py "Nombre" edad altura')
    