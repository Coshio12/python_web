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
#Y no haremos nada mas asi que colocamos pass y volveremos al main
class Cliente(Persona):
    pass

#Ahora vamos a aumentar a los metodos heredados mas informacion segun lo que necesitamos
#Creamos una clase empleado
class Empleado(Persona):
    #Creamos el constructor y le añadimos un atributo propio del objeto que sera sueldo
    def __init__(self, nombre, apellido,sueldo):
        #Usamos la funcion super para llamar y utilizar toda la informacion de la clase padre Persona
        super().__init__(nombre, apellido)
        #Persona.__init__(self, nombre, apellido) #Forma de heredar sin el super
        #Y inicializamos la variable propia del objeto
        self.sueldo = sueldo
    
    #Creamos un metodo para mostrar la informacion del empleadp
    def detalle_empleado(self):
        #Heredamos todo el metodo de detalle_persona
        super().detalle_persona()
        #Persona.detalle_persona(self) #Forma de heredar sin el super
        #Y le aumentados el print del sueldo
        print('Sueldo: ', self.sueldo)
    
    #Creamos el metodo para ver el estado del objeto
    def __str__(self):
        #en el return usamos la funcion super y concatenamos el valor de sueldo para mostrar la informacion
        return super().__str__() + f'\nSueldo: {self.sueldo}'
        #return Persona.__str__(self)+ f'\nSueldo: {self.sueldo}' #Forma de heredar sin el super

#Ahora con todo modificado volvemos al main