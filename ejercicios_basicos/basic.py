#Conceptos basicos de python

#CREACION DE VARIABLE
##Variable numerica
a = 5
print(a)

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
#Para el cociente de una division es con doble barra
#cociente = a //b 
print('----DIVISION----')
num3 = 50
num4 = 5
cociente = num3//num4
residuo = num3%num4

print(cociente)
print(residuo)

#Potencia
print('----POTENCIA----')
print(11**2)

#PARA REALIZAR PRINTS CON CADENAS DE CARACTERES SE TIENE QUE T