"""
    Como vimos en persona pudimos crear una clase con sus atributos y sus metodos
    pero es algo tedioso mostrar la informacion la informacion
    
    Para eso estan los constructores que son aquellos que inicializan las variables que seran utilizadas
    como atributos para guardar la informacion
"""
#Creamos la clase jugador
class Jugador:
    #Creamos el constructor con __init__ y que recibe como parametros self y los atributos que querramos
    #Recordando que se usa self para que el lenguaje entienda que dicho metodo es parte de una clase
    def __init__(self, nombre, dorsal):
        #llamamos a los parametros y les asignamos un valor igual a su nombre
        self.nombre = nombre
        self.dorsal = dorsal
    #Como pudiste observar ya no es necesario inicializar una variable con None, el constructor nos ahorra esa parte
    
    #Y creamos el metodo para mostrar la informacion
    def mostrar_datos(self):
        print('Nombre: ',self.nombre)
        print('Edad: ', self.dorsal)
        
    #Este metodo se ejecuta en vez de mostrar el espacio de metoria devolvera lo que este asignado dentro de un return
    # def __str__(self):
    #     return f'Nombre: {self.nombre}\nDorsal: {self.dorsal}'
    
        