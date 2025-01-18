#Primeramente creamos la clase Persona
class Persona:
    #Creamos las variables como forma de explicacion
    #Estas variables comentadas son publicas es decir que en cualquier parte del proyecto si esta importada
    #la clase se pueden modificar, cosa que eso se debe eviatr, para ello vamos a volverlos privados en un constructor
    # nombre = None
    # edad = None
    
    #Creamos el constructor con los parametros que reciben normalmente
    def __init__(self,nombre, edad):
        #para que una variable sea privada se la debe crear con doble barra baja al inicio de la variable
        #y asignarle el valor cuando se llame a la clase
        self.__nombre = nombre
        self.__edad = edad
    
    #Para demostrar que en la funcion anterior se crearon variables privadas, crearemos un metodo privado
    def __metodo_privado(self):
        print('Metodo privado')
    
    #Ahora si queremos modificar la informacion de un objeto si es necesario
    #Debemos simular la misma accion que en Java, es decir, crear los metodos, setters and getters
    #get_nombre se encargara de devikvedevolver el valor que tiene el get 
    def get_nombre(self):
        return self.__nombre
    #Y el metodo set recibe el nombre por el cual se quiere modificar la informacion
    #set es para modificar la informacion del objeto
    def set_nombre(self, nombre):
        self.__nombre = nombre
        
    #Dichos metodos se deben crear para cada atributo de la clase
    def get_edad(self):
        return self.__edad
    def set_edad(self, edad):
        self.__edad = edad
    
    #Y ahora con __str__ mostraremos el estado del objeto
    def __str__(self):
        return f'Nombre: {self.__nombre}\nEdad: {self.__edad}'
    