"""
    Ahora veremos el termino de polimorfismo
    En el paquete de herencia ya estabamos aplicando la logica de polimorfismo
    Que se basa en modificar o renombrear los metodos/variables de la clase padre
    Y poder utilizarlos sin problemas, obviamente recibiendo las variables de la misma clase padre
"""
#Creamos la clase padre
class Persona(object):
    #Creamos el constructor con un atributo
    def __init__(self,nombre):
        self.nombre = nombre
    
    #Creamos un metodo basico
    def moverse(self):
        print('Caminando')

#Creamos una sub-clase que herede la informacion de Persona
class Atleta(Persona):
    #Reescribimos la funcionalidad del metodo de la clase padre
    def moverse(self):
        print('Correriendo')

#Creamos una sub-clase que herede la informacion de Persona
class Ciclista(Persona):
    #Reescribimos la funcionalidad del metodo de la clase padre
    def moverse(self):
        print('Manejando bicicleta')
    