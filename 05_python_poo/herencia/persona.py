#Creamos la clase persona
class Persona:
    #Creamos el constructor
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
    
    #Creamos el metodo que mostrara la informacion
    def detalle_persona(self):
        print(f'Nombre: {self.nombre} \nApellido: {self.apellido}')
    
    #Y creamos el metodo para ver el estado del objeto
    def __str__(self):
        return f'Nombre: {self.nombre} \nApellido: {self.apellido}'

#Ahora crearemos una clase que recibe como parametro la clase padre en este caso Persona
#Y no haremos nada mas asi que colocamos pass
class Cliente(Persona):
    pass
