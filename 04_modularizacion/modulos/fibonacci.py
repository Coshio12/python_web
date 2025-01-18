#Como modularizacion podemos entender que son scripts o archivos .py
#El cual tienen las diferentes operaciones que se haran dentro del sistema
#Esto permite separar el sistema en varias partes

#Definimos la funcion que hara la operacion de la sere de fibonacci
#Recibe como parametro el numero
def fibo(numero):
    #Se crean dos variables
    a, b = 0 , 1
    #En un bucle creamos la serie de fibonacci
    while a < numero:
        #Este bucle hara el calculo y imprimira directamente cada uno de los resultados
        print(a, end=' ')
        a, b = b, a + b
    print()

#Creamos otra funcion de la serie de fibonacci
#Lo diferente sera que estamos guardando la informacion o los resultados de la serie en una lista
def fibo2(numero):
    resultado = []
    a, b = 0 , 1
    while a < numero:
        resultado.append(a)
        a, b = b, a + b
    
    return resultado
#Apartir de aqui llamaremos las funciones desde otro archivo