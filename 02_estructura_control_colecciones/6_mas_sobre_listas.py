"""
    Las variales del tipo lista son muy versatiles
    y suelen ser muy usadas para realizar diferentes aplicaciones
    por eso, es importante saber los diferentes metodos que tiene
    los de este archivo son los mas comunes
"""
#Declaramos dos variables variable
print('='*45)
print('VARIABLES INICIALES')
datos = ['Jose', 23, "Basket"]
X = 'HOLA'
print(datos)
print(X)

#El metodo append agrega al final de la lista un valor
#que este dentro del parentesis
print('='*45)
print('APPEND')
datos.append('Cossio')
print(datos)

#El metodo extend como el nombre lo dice
#Extiendo el tamaño de la variable
#Si le pasamos al metodo la variable X que tiene una cadena de texto
#Colocara cada caracter en una posicion distinta: "H","O","L","A"
print('='*45)
print('EXTEND')

datos.extend(X)
print(datos)
#Si le pasamos la variable datos, agregara los valores a la lista
#Es la misma variable escrita dos veces
datos.extend(datos)
print(datos)

#El metodo insert tiene dos parametros
#El primero es la posicion donde queremos agregar un dato
#Y el segundo parametro, es el valor/dato que queremos agregar a la lista
#En este caso agregamos en la posicion 0 el numero 100
datos.insert(0,100)#1 posicion, 2 valor
print(datos)

#Volvemos a declarar la variable
datos = ['Jose','Alejandro', 23, "Basket"]

print('='*45)
print('REMOVE')

#El metodo remove quita el valor que esta dentro del parentesis
#En este caso es la cadena de texto 'Jose'
#Si se desea sacar un entero es simplemente pasarle el numero sin comillas
datos.remove('Jose')
print(datos)

#El metodo pop no es obligatorio pasarle un parametro
print('='*45)
print('POP')

#Al no pasarle ningun parametro borrara el ultimo valor de la lista, en este caso
#Basket
#Si queremos pasarle un parametro debe ser un entero
#Que hara la misma accion que el remove, es decir
#Borrara el dato en la posicion que reciba
datos.pop()
print(datos)

#El metodo clear simplemente elimina todos los datos de la lista
print('='*45)
print('CLEAR')

#Es decir que devolvera una lista vacio = []
datos.clear()
print(datos)

#Volvemos a declarar la lista
datos = ['Jose','Alejandro', 23, "Basket",23,23]

#El metodo index señala en que posicion esta el valor deseado
print('='*45)
print('INDEX')

#Es decir que recibe como parametro algun valor de la lista
#Entero: 23 o caracter: 'Jose'
#Y devolvera la posicion en este caso 2
A = datos.index(23)
print(A)

#El metodo count cuenta la cantidad de veces que se repite un valor
print('='*45)
print('COUNT')

#Le pasamos como parametro 23 y devolvera la cantidad de veces que se repite
#En este caso 3
D = datos.count(23)
print(D)

#Creamos una lista de frutas
frutas = ['Naranja', 'Pera', 'Manzana', 'Uva','Palta']

print('='*45)
print('SORT')


#Lo que hace este metodo es ordenar por orden alfabetico los valores de la lista
frutas.sort()
print(frutas)

#Creamos una lista de numeros
numeros = [1,2,3,4,5]

#El metodo reverse no recibe parametros
print('='*45)
print('REVERSE')

#Su funcion es ordenar los datos del ultimo al primero
numeros.reverse()
print(numeros)

#El metodo copy simplemente copia los valores de una lista ya creada
print('='*45)
print('COPY')


numeros_2 = numeros.copy()
print(numeros_2)
