"""
    Los conjuntos son variables que tambien son listas pero funcionan de otra manera
    Tienen diferentes metodos para crearse
    No guardar datos iguales
    No respetan un orden
"""
#Definiendo un conjunto vacio
A = set()
print(type(A)) #Nos muestra que es del tipo set

#Otra forma de crear un conjunto es con llaves
B = {'a','b','c'}
print(type(B)) #Tambien nos muestra que es del tipo set
print(B) #Nos muestra el contenido de la variable

#Podemos llevar a un conjunto una cadena de texto
#Al ser un conjunto que no guarda variables repetidas
#solo guardara la letra "a" solo una vez
C = set('abracadabra')
print(C)

#Lo mismo pasa en este caso
D = set('alakazam')
print(D)

#Operadores
#Hay varios operadores que se pueden usar para trabajar con conjuntos
#El signo - muestra datos que estan B pero no en C
res = B - C
print(res)

#El signo | devuelve letras en B o en C
res = B | C
print(res)

#El signo & devolvera letras que estan tanto en B como en C
res = B & C
print(res)

#El signo ^ devuelve las letras en B o en C pero no en ambas
res = B ^ C
print(res)

#Tambien se pueden usar metodos con los conjuntos
#Creamos un nuevo conjunto
A = {'a', 'b', 'c'}

#Usamos el metodo add para agregar un nuevo valor
#Pero si dicho valor ya existe en el conjunto
#No lo guardara
A.add('d')
print(A)

#Usaremos el metodo discard si queremos borrar algun dato del conjuntio
#para ello tenemos que pasarle el valor que queremos quitar
A.discard('b')
print(A)

#Usaremos el metodo clear para borrar todos los datos del conjunto
A.clear()
print(A)
