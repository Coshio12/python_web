"""
    Una vez explicado las bases de python ahora vamos a hacer cosas mas avanzadas para crear
    una pagina web con python.
    
    Usaremos Flask:
    
    Pero para poder usar la tecnologia tenemos que entender lo que es una funcion decoradora
    y como se aplicara para una parte del codigo que se meostrara    
"""

#Para ello vamos a crear una funcion decorador que reciba una funcion
def decorador(func):
    
    #Dentro tambien crearemos una funcion decorar que reciba n argumentos
    def decorar(*args):
        #Que simplemente se mostrara un mensaje de ejecucicion de la funcion
        print('Inicia la ejecucion de la funcion: ',func.__name__)
        #Se llamara a la funcion con n argumentos
        func(*args)
        #Se mostrara un mensaje que ya termino la funcion
        print('Termina la ejecucion de la funcion: ',func.__name__)
        
    #Y se retornara la funcion decorar
    return decorar

#El truco esta que tenemos que llamar a decorar, para ello primeramente tenemos que crear una funcion aparte al decorador
#Y al usar arroba haciendo incapie al decorador llamamos las funciones con el parametro que querramos
#De esa forma se ejecutara el primer mensaje de decorar, de ahi la funcion y de nuevo el mensaje de decorar
#Cumpliendo las condiciones de decorar

#Llamamos a decorador
@decorador
#Creamos una funcion que reciba como parametro el nombre
def hola(nombre):
    #Imprimimos un mensaje
    print('Hola mundo ' ,nombre)

#Lo mismo hacemos si queremos con una operacion aritmetica
@decorador
def suma(a,b):
    suma = a + b
    print('La suma es: ',suma)

#Lllamos a las funciones mandando los argumentos
hola('Cossio')

suma(10,20)


'''
    De esta forma vemos como funciona la logica de decorador en python
'''
