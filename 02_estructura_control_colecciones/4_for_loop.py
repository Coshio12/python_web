"""
    El bucle for es aquel para poder manejar de manera interactica por indices
    la informacion de diferentes listas o si se quiere realizar diferentes
    acciones segun la cantidad de veces que sea necesario
"""
datos = ['Jose', 'Alejandro', 25, 35.4, True]

#La estructura es basica usando la pabara reservada "in"
#Para poder movernos dentro de la lista
for dato in datos:
    print(dato)
#Este for imprive todos los datos que estan dentro de la lista

#Es verdad que tambien se puede usar el bucle while
#Pero seria crear mas codigo, por ello para ciertas ocasiones
#Es mejor el bucle for
C= 0
print('while')
while C< len(datos):
    print(datos[C])
    C+=1
#Este while se mueve por la lista segun la cantidad de valores
#y segun el valor incremental que se usa para realizar las iteraciones

#Tambien se puede usar el metodo range()
#que tiene dos maneras
#La primera es para que se ejecute segun un numero determinado de veces
#En este caso seria de 10, se imprimira el valor de 0 a 9
for n in range(10):
    print(n)

#y si se coloca dos numeros, el primero sera el valor inicial
#y el segundo el valor donde terminara la ejecucion
#Es decir, devolvera valores desde el 10 hasta el 19
for n in range(10,20):
    print(n)
