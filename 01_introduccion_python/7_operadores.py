#OPERADORES RELACIONALES
#Los operadores relacionales son aquellos que se usan para comparar la informacion entre las variables
#Devolviendo un valor booleano true (si se la comparacion es verdadera) y false (si la comparacion es falsa)

#Casos con variables numericas
print('='*45)
print('OPERADORES RELACIONALES')
print('='*45)
numero_1 = 15
numero_2 = 90
numero_3 = 15

#Operador de igualdad, solamente devolvera  true si los valores son 100% iguales
print(numero_1 == numero_2) #devuelve false
print(numero_1 == numero_3) #devuelve true

#Otra forma es con el signo de exclamacion y un igual
#Que nos dice que las variables son diferentes, es como negar el valor de una variable
print(numero_1 != numero_2) #Resultado true

#Al ser valores numericos tambien podemos comparar con los signos de
#mayor, menor, mayor o igual, menor o igual
print(numero_1 > numero_2) #Resultado False
print(numero_1 < numero_2) #Resultado True
print(numero_1 >= numero_2) #Resultado False
print(numero_1 <= numero_2) #Resultado True

#Tambien se puede usar estos signos para realizar comparaciones con cadenas de texto
palabra_1 = 'HOLA'
palabra_2 = 'hola'
palabra_3 = 'hola '

#Tener en cuenta que depende muchisimo el valor de las variables para devolver un true
#Las variables con cadenas de texto son mas extrictas al momento de trabajar con ellas
print(palabra_1 == palabra_2) #Resultado False
print(palabra_1 != palabra_2) #Resultado True
print(palabra_2 == palabra_3) #Resultado False

#Al ser variables mas estrictas las que tienen cadenas de texto, el condenido puede ser igual
#Pero si se tiene un espacio dentro de la variable, al momento de comparar, se lo toma como un valor diferente

#OPERADORES LOGICOS
#Operador NOT, es aquella que niega la informacion de una variable
print('='*45)
print('OPERADORES LOGICOS')
print('='*45)
print(not True) #Resultado False
print(not False) #Resultado True

#Operador AND, es aquella que compara dos condiciones que si son verdaderas devuelve True, si no, False
print(True and True) #Resultado True
print(True and False) #Resultado False

#Operador OR, es aquella que devuelve True si al menos una condicion sea verdadera
a = 10
b = 5

#El primer parentesis devuelve false porque no son iguales
#El segundo parentesis devuelve true porque son diferentes
#El resultado final es False, porque True y False es False debido a la expresion and, daria true si ambos casos son iguales
print((a==b) and (a != b)) #Resultado False

#El primer parentesis devuelve false porque no son iguales
#El segundo parentesis devuelve true porque son diferentes
#El resultado final es true porque por el operador OR señala que existe almenos un True
print((a==b) or (a != b)) #Resultado True

#El primer parentesis devuelve false porque no son iguales
#El segundo parentesis devuelve true porque son diferentes
#El resultado final es false por que al haber un operador not niega el resultado
print((a==b) or not(a != b)) #Resultado False

#EXPRESION ANIDADA
numero_a = 10
numero_b = 5

#Primero resuelve los parentesis, despues operador aritmetico y por ultimo operadores logicos
expresion= numero_a * numero_b - 2 ** numero_b >= 20 and not (numero_a % numero_b) !=0
print('='*45)
print('EXPRESION ANIDADA')
print('='*45)
print(expresion)
