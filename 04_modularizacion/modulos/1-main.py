#En este archivo main lo que haremos sera importar el archivo de fibonacci
#de la misma manera que estuvimos haciendo hasta ahora
import fibonacci

#Si colocamos fibonacci y un . nos mostrara las funciones que podemos usar
#Entonces mostramos el resultado de cada una de las funciones que creamos
fibonacci.fibo(100)

print('Fibo',fibonacci.fibo2(100))

#NOTA: Hay diferentes formas de importar modulos
#Uno de ellos es desde from importamos las funciones de fibonacci
from fibonacci import fibo, fibo2

#Y de esta forma seria como llamar a cualquier funcion de python
fibo(150)
print(fibo2(150))

#Si queremos importar directamente todas las funciones colocamos *
from fibonacci import *

#Y llamamos a las funciones de la misma manera
fibo(250)
print(fibo2(250))

#Tambien podemos usar el "as" para colocarle un alias al modulo que se esta importanto
#Se suele utilizar para saimplificar nombres muy complicados
import fibonacci as fib

#Y para llamar a las funciones se llama primero al alias y despues al metodo
fib.fibo(350)
print(fib.fibo2(350))

#Si solo queremos una funcion del metodo podemos tambien agregarle un alis
from fibonacci import fibo as f1
from fibonacci import fibo2 as f2
f1(650)
print(f2(650))

#Siguiendo el tema de los modulos, exixte una funcion que nos da la informacion que contiene un modulo
#Como ser funciones, etc
#Esta es la funcion dir que puede recibir como parametros las librerias que deseamos importar 
#Por ejemplo vamos a importar el modulo de fibonacci
import fibonacci

#Y vamos a pasarle a la funcion fibonacci
print(dir(fibonacci))
#Lo que nos devuelve es esto:
#['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'fibo', 'fibo2']
#Dandonos a conocer todo lo que contiene fibonacci

#Tambien podemos hacerlo con sys que lo vimos en otro archivo (entra-script.py)
import sys
print(dir(sys))
print('='*45)
#Ejecutalo para ver el resultado que es una lista de todo lo que contiene
#Hacemos lo mismo con otro modulo
import builtins
print(dir(builtins))
print('='*45)

#O tambien podemos solo imprimir dir() sin ningun argumento
print(dir())

#NOTA: ESTE ARCHIVO ESTA SIGUIENDO MALAS PRACTICAS DE CODIGO LIMPIO
#SE LO CREO DE ESA FORMA PARA SEGUIR UNA COHERENCIA Y FACIL ENTENDIMIENTO
