#Este archivos nos mostrara las diferentes acciones que se pueden hacer con los caracteres.

#Primeramente creamos una variable
TEXTO = "Hola"

#Multiplicacion de caracteres
MULTIPLICAR_CARACTERES = TEXTO * 3
print(MULTIPLICAR_CARACTERES)
#El resultado es la cadena de texto repetida la cantidad de veces segun el multiplicador

#Sumar con caracteres
SUMA = TEXTO + " buenos dias"
print(SUMA)
#El resultado es que al texto original se le agrega la cadena de texto nueva que se indica

#Indexar caracteres
#Una forma de trabajar con caracteres es con el index
#En el ejemplo se ve que python tiene 7 letras que comienza de 0 a 6
#Tambien se puede comenzar con numeros negativos siendo el -1 el ultimo caracter y -6 el primer
#+-+-+-+-+-+-+-+-+-+-+-+-+
#| p | y | t | h | o | n |
#+-+-+-+-+-+-+-+-+-+-+-+-+
#0   1   2  3    4   5   6 
#-6 -5  -4 -3   -2  -1
PALABRA = 'python'
print(PALABRA)
print(PALABRA[0]) #nos mostraria la primera letra
print(PALABRA[-1]) #muestra la ultima letra

#Slicing o segmentacion
#El slicing o segmentacion es aquel que se usa para tomar ciertos caracteres de la la palabra poder trabajar con ellos
#en vez de tomar letra por letra  o toda la palabra
print(PALABRA[0:3])#muestra desde el inicio hasta la 3 letra
print(PALABRA[:3])#muestra desde la primera letra hasta la 3 letra
print(PALABRA[3:])#muestra desde la 4 hasta el final
PALABRA2 = "S" + PALABRA[1:] #añado la letra s al inicio y mediante slicing selecciono desde la posicion 1 hasta el final de la palabra
print(PALABRA2)

#len
#len es un metodo o palabra reservada que tiene una funcion
#en este caso es devolvernos la cantidad de letras/caracteres que tiene la palabnra
print(len(PALABRA))
