#PARAMETROS Y ARGUMENTOS
#Los parametros son aquellos valores que se declaran en la misma linea que la funcion
#Son variables que se recibiran informacion y se podran usar dentro de la funcion
#Para poder realizar diferentes operaciones
def saludo(nombre):#Nombre es un para metro
    edad = 25
    return f'Hola, {nombre} desde la funcion SALUDO'

#Estas funciones reciben dos parametros
def sumar(numero1, numero2): 
    return numero1 + numero2

def restar(numero1, numero2):
    return numero1- numero2

#Esta funcion tiene parametros por defecto
#Se puede colocar valores por defectos a los parametros de una funcion
#Es una manera de poder asegurar que las funciones estan correctamente creadas
#Preveendo que exista error de creacion de argumentos
def restando(a = None, b = None): #parametros por defecto
    if a == None or b == None:
        print('Debes enviar dos numeros a la funcion')
        return
    return a - b

#Los argumentos son aquellos valores que se les pasa a las funciones cuando las estamos llamando
#La siguiente es un argumento basico, simplemente le pasamos una cadena de texto
saludando = saludo('Alejandro') 
print(saludando)

#Tambien tenemos los argumentos por posicion
#Esto quiere decir que el primer argumento ira como primer parametro dentro de la funcion que se esta llamando
#Y el segundo ira al siguiente parametro creado en la funcion
suma = sumar(12,8) #argumentos por posicion
print(suma)

#Tambien hay argumentos por nombre
#Podemos hacer incapie en esta parte del codigo
#A los parametros de las funciones y asignarles un valor determinado
#Es decir que la funcion resta funcione correctamente
#Primero hay que pasarle un numero bajo al segundo parametro y uno alto al primer parametro
resta = restar(numero2=20, numero1=40) 
print(resta)

#Tambien hay argumentos por defecto
#Este tipo va de la mano con los parametros creados por defecto
#Permitiendo que si a la funcion creada no se le pasa ningun valor
#Este se ejecute con normalidad
#Es una forma para poder trabajar con el usuario
#Anticipando los valores que podria colocar dentro de un sistema
resta = restando() 
print(resta)
