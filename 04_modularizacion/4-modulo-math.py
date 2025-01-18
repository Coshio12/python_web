"""
    En python hacer ciertas operaciones matematicas es relativamente facil
    pero se puede dar el caso que se necesiten otros calculos
    Para ello existe el modulo math
"""
#Importamos el modulo y le damos un alias
import math as m

#PARA DECIMALES
#floor es una forma de redondear el numero que se pase ignorando si es un .99
#Devolviendo el valor entero solamente, es decir, redondea hacia abajo
print(m.floor(4.99))
#ceil hace lo contrario que floor, es un redondeo hacia arriba pero 
#a pesar de estar con decimales .01 devolvera un valor +1 del entero del decimal
print(m.ceil(4.01))#arriba

#Creamos una lista
n = [0.9999, 1, 2,3]
#fsum, suma los valores de la lista respetando los decimales
print(m.fsum(n))

#trunc es aquel metodo que redondea ifnorando todos los decimales
print(m.trunc(45.785))

#pow sirve para realizar potencias pasandole como primer argumento el numero deseado y 
#como segundo argumento el numero a la que se quiere elevar
print(m.pow(2,3))

#sqrt saca la raiz cuadrada de un numero respetando los metodos matematicos
#es decir que la funcion dara error y si se pasa el valor 0 o valores negativos
print(m.sqrt(16))#raiz cuadrada

#pi devuelve el valor de pi
print(m.pi)

#e devuelve el valor de euler
print(m.e)

#El modulo math tiene muchos mas metodos hay que recurrir a la documentacion si se quiere sabber mas
