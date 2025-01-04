#Conceptos basicos de python

#CREACION DE VARIABLE
#Las variables se pueden crear de la manera tradicional un nombre y el valor
n = 10
a = 'hola'
print(f'{n} - {a}') #Al gregar una f al inicio del print nos permite colocar diferentes variebles dentro de la funcion print y mostrarlos de una manera mas comoda
print(n,a)

#Tambien se puede crear varias variables en la misma linea
c,v,b = 10, 'hola', 5
print(c,v,b)

#Se puede cambiar los valores de variables ya creadas
k = c
print(f'k = {k}')
k = 50
print(f'k despues del cambio es {k}')

##Cadena de caracteres
b = 'cadena de texto'

###Recalcar que la manera de crear variables numericas no van con comillas, en cambio para las
###variables de texto pueden ir comillas simples o comillas dobles
###Es importante recalcar que las variables escritas una con mayus y otra con minus
###Son totalmente diferentes, es decir, cada variable se crea y guarda un valor

c = 123
C = 'texto'

print(f'{c} y {C}')

#Operaciones aritmeticas

#Suma
##Desde la consola se pueden sumar valores numericos de manera directa sin la necesidad de crear variables
##Dentro de un IDE es mejor guardar la informacion dentro de una variable
print('----SUMA----')
num1 = 123
num2 = 123

print(num1+num2)

#Tambien se puede guardar el resultado dentro de una variable
suma = num1+num2

print(suma)
#Resta
print('----RESTA----')
resta = num1 - num2

print(resta)
#multiplicacion
print('----MULTIPLICACION----')
producto = num1 * num2

print(producto)

#Division
print('----DIVISION----')
num3 = 50
num4 = 6
division = num3/num4
residuo = num3%num4 #muestra el residuo de la operacion

print(division)
print(residuo)

#Potencia de un numero
print('----POTENCIA----')
print(11**2)

#Estas son las principales operaciones aritmeticas clasicas realizadas en el lenguaje de python
