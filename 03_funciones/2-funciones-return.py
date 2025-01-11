#Retornando valores
#La frase de retornar valores hace incapie a que a partir de una funcion podamos retornar los valores
#Es decir, que dentro de una funcion se ejecuten todas las operaciones deseadas
#Y la misma funcion las devuelva
#Para ello se usara la palabra reservada de return, que permite retornar un valor final

#Definimos la nueva funcion
def retorno():
    #Definimos las variables
    global nombre_2
    nombre_2 = 'Jose Cossio'
    edad = 23
    #Retornamos un saludo, el nombre y la edad
    return 'Hola desde la funcion saludar ', nombre_2, edad

#Podemos retornar el valor de la funcion solamente llamando dicha funcion dentro de un print
print(retorno())

#Podemos crear una variable y guardar la informacion de la funcion dentro de ella
#En este caso seria una tupla ya que esta recibiendo 3 valores distintos
valor = retorno() 
print(valor)

#Al retornar una tupla, podemos crear varias variables para que guarden cada valor de la tupla
saludo, nombre, edad = retorno()
#Y podemos imprimirla en un print formateando la infomacion
print(f'El saludo "{saludo}" el nombre es: {nombre} y la edad {edad}')
