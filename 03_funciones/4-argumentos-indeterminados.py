#Cuando no sabemos cuantos argumentos tendra, por posicion
"""
    En el archivo anterior vimos lo que son los diferentes tipos de argumentos que puede recibir una funcion
    Permitiendo operar y usar las funciones de diferentes maneras
    
    Ahora veremos un caso especial, que es cuando no sabemos cuantos parametros se le mandaran a la funcion creada
    para ello usaremos los argumentos indeterminados.
    
"""
#Cuando se crea una funcion con un parametro con una palabra reservada como args acompañada con asterisco
#Nos muestras como la funcion podra recibir "n" numeros dentro de la funcion
#En este caso veremops lo que son n numeros enteros que puede recibir una funcion
#Tomando en cuenta que la funcion detectara los numeros como si fuera argumentos o parametros por posicion
def suma(*args): #*args permite que la funcion reciba diferentes numeros
    suma = 0
    #Al tener varios numeros denrto de la funcion lo que debemos hacer es recorrer con un for para poder realizar
    #Las operaciones necesarias
    for index in args:
        suma += index
    return suma

#Despues en la siguiente linea podemos ver como le pasamos varios argumentos a la funcion para que realice
#Una operacion en este caso una suma
suma_total = suma(1,2,3,4,5)
#y al mostrarlo en consola vemos como imprime el resultado sin problemas
print(f'la suma total es: {suma_total}')

#Argumentos por nombre
#Tambien podemos enviarle textos, en este caso estamos pasando tanto numeros como cadenas de texto
#Para los cadenas de texto a la funcion hay que enviarle como parametro junto con los asteriscos
#la palabra reservada kwargs
def suma_1(*args, **kwargs):
    suma = 0
    for index in args:
        suma += index
    #Tenemos que agregar en el return la palabra kwargs para demostrar que estamos usando las cadenas de texto
    return suma, kwargs

#Creamos dos variables para poder guardar la informacion que es la suma de los diferentes argumentos 
#y de la misma manera las cadenas de texto
#siguiendo la logica los argumentos por nombre
suma_total,datos = suma_1(10,20,3,100, nombre = 'Jose', edad = 25)
#Mostramos la suma como en la anterior funcion
print('La suma total es: ', suma_total)
#Y mostramos los datos
#Los datos en este tipo de funciones se guardarian como un diccionario
#Tomando el nombre como key y jose como valor
#edad como key y 25 como valor
print(datos)