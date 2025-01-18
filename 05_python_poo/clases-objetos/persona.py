"""
    CREAMOS NUESTRA CLASE
    Como dijimos en main.py una clase es el molde para generar informacion
    que contiene objetos fisicos y conceptuales
    
    Por ejemplo: Tenemos persona, una persona puede tener muchos atributos, entre esos puede ser
    el nombre, edad, altura, peso, etc. y podemos usar esa informacion para generar diferentes metodos que serian
    los objetos conceptuales
"""
#Para crear una clase usamos la palabra reservada class y despues el nombre con la primera letra en 
#MAYUSCULA
class Persona:
    #Creamos los diferentes atributos
    #Los atributos o objetos fisicos, son las variables donde se almacenara la informacion
    #Para ello es mas practico que la variable se inicie con el valor None
    nombre = None
    edad = None
    
    #Despues creamos el comportamiento o metodos de la clase
    #Que serian los objetos conceptuales
    #Se crean estos metodos como si fuese una funcion con la palabra reservada def, despues el nombre del metodo
    #Pero debe recibir como parametro por mera constumbre la palabra reserva "self"
    #Dicha palabra ayuda a que el lenguaje entienda que la funcion pertenece a la clase en este caso a Persona
    def mostrar_datos(self):
        #Creamos un metodo que simplemente muestra los datos
        #Para poder concatenar la informacion debemos usar self para poder llamar la informacion de las variables creadas
        print('Nombre: ',self.nombre)
        print('Edad: ', self.edad)

    #Volvemos al main.py
