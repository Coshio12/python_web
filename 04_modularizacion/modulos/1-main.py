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
