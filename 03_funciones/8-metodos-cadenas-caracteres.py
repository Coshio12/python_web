"""
    Como en el archivo anterior tyambien vimos diferentes tipos 
    de metodos/funciones que se pueden usar con cadenas de texto
    ahora veremos otras funciones para las cadenas de texto
"""
#Primero tenemos la cadena de texto despues un punto y el metodo upper
#Este metodo convierte todo el texto a mayusculas
print('Hola mundo'.upper())

#Este metodo convierte todo el texto a minusculas
print('HOLA MUNDO'.lower())

#Este metodo vuelve la primera letra de la cadena de texto a mayuscula
print('hola mundo '.capitalize())

#Este metodo convierte la primera detra de cada texto a mayuscula
print('hola mundo'.title())

#Este metodo cuenta la cantidad de veces que aparece una letra que le pasa como argumento
print('Hola mundo'.count('o'))

#Se define una variable con una cadena de texto
palabra = 'Python'
#Este metodo recibe dos argumentos el primero es la letra que se quiere reemplazar y la otra es la letra que va a sustituir
#a la que se quiere reemplazar
palabra = palabra.replace('P','S')
print(palabra)

a = 'P Y T H O N'.replace(' ','')
print(a)

#Este metodo elimina los espacios agregados antes de la cadena de texto
h = '   Hola Mundo  '.strip()
print(h)

#Este metodo si se le pasa un argumentos eliminara dicho caracter antes de la cadena de texto
h = '---------Hola - Mundo----------'.strip('-')
print(h)

#Este metodo coloca cada palabra como un dato de una lista
h = 'Hola Mundo'.split()
print(h)

#Este metodo cada que encuentra un valor de la funcion con el argumento lo
#lo colocara en un dato en una lista
h = 'Hola,Mundo,de,python'.split(',')
print(h)

#Los siguientes metodos pregunta si la cadena de texto cumple dicha funcion
#si tiene la primera letra en minuscula
print('Hola'.islower())
print('hola'.islower())
#si tiene la primera letra en mayuscula
print('Hola'.isupper())
print('HOLA'.islower())
#si es un titulo
print('Hola Mundo'.istitle())
print('hola mundo'.istitle())
#si tiene espacios
print('           '.isspace())
print('      s     '.isspace())
