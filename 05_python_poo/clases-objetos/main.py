"""
    Programaicion Orientada a objetos:
    
    En esta seccion analizaremos todo acerca de la programacion orientada a objetos
    
    Primero debemos entender que es una clase y que es un objeto
    Clase: Es el molde para crear un objeto compuesto por objetos fisicos(atributos) y conceptuales(metodos)
    Objeto: Es el producto de aplicar el molde de la clase
    
    Para ello vamos a ir al archivo persona.py
"""
#Volviendo desde persona.py
#Lo primero que debemos hacer es importar la clase
#para ello llamamos desde persona.py y importamos la clase Persona
from persona import Persona
#Ahora siguiendo con el objeto jugador vamos a explicar que son los constructores
#ir a jugador.py
from jugador import Jugador

#Creamos un objeto
#Creando la variable y que tenga la informacion Persona(), significa que la variable sera del tipo persona.Persona
persona1 = Persona()
#Ahora asignamos los valores segun los atributos de persona con el nombre de la variable donde guardamos la informacion
#de la clase y con un punto llamamos al atributo de la clase y le asignamos un valor 
persona1.nombre = 'Alejandro'
persona1.edad = 23

#Lo mismo con persona2
persona2 = Persona()
persona2.nombre = 'Adriana'
persona2.edad = 22

#Ahora llamamos al metodo creado que era mostrar datos que no recibia ningun otro argumento ademos del self
persona1.mostrar_datos()
print('='*45)
persona2.mostrar_datos()

#De esta forma podemos crear clases y objetos con python ademas cuando se ejecute por primera vez
#Se creara la carpeta de archivos compilados __pycache__

#Ahora usando los constructores creamos diferentes objetos
jugador1 = Jugador('Michael',23)
jugador1.mostrar_datos()

jugador2 = Jugador('Ginobili',20)
jugador2.mostrar_datos()

#Pudiendo observar que con menos lineas de codigo hicimos lo mismo que en el codigo anterior

#Ahora si te dio la curiosidad de que imprime por consola si solo le pasamos el jugador1
print(jugador1) #<jugador.Jugador object at 0x00000235B0126BA0>
#Nos devuelve el espacio de memoria que se le fue asignasdo
#Lo podemos cambiar para que imprima el formato asignado creadun un metodo __str__
#Que esta comentado en jugador.py
