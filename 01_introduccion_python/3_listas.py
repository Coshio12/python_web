#Las listas son aquellas que son utilizadas para guardar varios valores dentro de una sola variable
#Dichas listas pueden tener tanto valroes numericos como cadenas de texto.
squares = [1,2,3,4,5]
print(squares)

#Tambien podemos seleccionar un valor en especifico de la lista
print(squares[2]) #mestra el valor en la posicion 2
#NOTA: las posiciones comienzan siempre desde el 0 hasta el ultimo valor

#Tambien podemos usar el slicing para trabajar con estas listas

opcion1 = squares[1:3] #Muestra desde el valor de la posicion 1 hasta el valor de la posicion 3
opcion2 = squares[:4] #Muestra el valor desde la posicion 0 hasta en este caso la posicion 4
opcion3 = squares[2:] #Muestra desde la posicion 2 hasta el ultimo valor de la lista

print(opcion1)
print(opcion2)
print(opcion3)

#Diferentes tipos de datos
datos = ['Jose', 25, 'Bolivia']
print(datos)
#Podemos mostrar los diferentes datos usando los indices y el slicing
print(datos[0])
print(datos[:2])
#Las listas son mutables, es decir, se pueden cambiar los valores de las listas
datos[0] = 'Alejandro'
print(datos)
#Tambien podemos agregar datos con el metodo append
datos.append(1.80)
print(datos)

#Tambien podemos usar el metodo len para saber cuantos elementos tiene la lista
print(len(datos))

#Operaciones con listas
datos_completos = datos + squares #guardara la informacion de las variables datos y squares en la variables datos_completos

datos_mult = datos * 3 #dara como resultado el valor de la variable datos 3 veces

print(datos_completos)
print(datos_mult)

#EXTRA: El metodo type, nos ayuda a saber el tipo de dato de una variable
print(type(datos))

#tambien podemos concatenar tipos de datos en una sola variable usando la coma

nombre = 'Jose Cossio'
edad = 23

datos2 = nombre, edad
print(type(datos2)) #Se vuelve una tupla

#Podemos tambien formatear la informacion es decir, aplicar una forma para mostrar de una mejor manera la informacion
print(f'Nombre: {nombre} \nEdad: {edad}') #Suele ser una manera mas comoda para mostrar la informacion con el print
