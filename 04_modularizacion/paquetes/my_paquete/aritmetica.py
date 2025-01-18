#Definimos la funcion sumar con valores de una lista de n numeros
def sumar(*args):
    #Se crea la variable de resultados
    suma = 0
    #Se crea el bucle que sumara todos los numeros de una lista
    for n in args:
        #se suman los valores y se guardan en la variable creada
        suma += n
    #Se retorna la variable
    return suma

#Creamos una variable que con ayuda de lambda recibira datos y los restara
restar = lambda a,b: a - b

#Creamos una variable que con ayuda de lambda recibira datos y creara una potencia
potencia = lambda a,b: a ** b
