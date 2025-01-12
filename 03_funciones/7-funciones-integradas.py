"""
    Funciones integradas
    Las funciones integradas son aquellas que llegan con el propio lenguaje
    Durante los diferentes archivos y secciones que se crearon se estuvieron utilizando dichas funciones
"""
#Repasando algunas

#Esta funcion vuelve una cadena de texto a entero
print(int('15'))

#Esta funcion vuelve una cadena de texto a flotante
print(float('45'))

#Esta funcion vuelve un numero a cadena de texto
print(str(45))

#La funcion len devuelve el tamano de una cadena de texto o la cantidad de elementos guardados en
#una lista, diccionario, tupla
print(len('Python'))

#La funcion round redondea un valor flotante
print(round(12.5))

#la funcion round con dos argumentos el primero lo redondea y el segundo es la cantidad de decimales que se desea
print(round(12.548941235456,3))

#Eval evalua si dentro de una cadena de texto existe una operacion
#En este caso devolvera el resultado de la suma
print(eval('2 + 5'))

#Definimos una variable
n = 10
#Eval detecta si existe una variable para poder realizar una operacion
print(eval('n * 10 - 5'))

#pero si la variable no existe como en este caso devolvera un error
#indicando que a no esta definida
#print(eval('a * 10 - 5'))

#La siguiente funcion saca el valor absoluto de un numero
print(abs(-35))

#La siguiente funcion convierte un numero en binario
print(bin(10))

#la siguiente funcion convierte un numero binario a entero
print(int(0b1010))

#La siguiente funcion convierte un numero en hexadecimal
print(hex(10))

#la siguiente funcion convierte un numero hexadecimal a entero
print(int(0xa))

#muestra mensajes de apoyo sobre el lenguaje
#print(help())
