"""
    En esta carpeta hablaremos del encapsulamiento
    Es aquella forma de proteger las variables de clases y que no se puedan modificar de manera facil
    En otros lenguajes como Java existe una palabra clave "private" pero en python
    Lo que debemos hacer es simular la misma logica que usa java para realizar el encapsulamiento
    Antes de ver el codigo de main ir persona.py
"""
#Importados desde persona la clase Persona
from persona import Persona

#Construimos el objeto
persona1 = Persona('Jose',23)
print(persona1)
print('='*45)
#Si descomentamos la siguiente linea, python va a ignorar que se esta tratando de acceder a la informacion del objeto
#por el cual no mostrara la nueva informacion
#persona1.__nombre = 'Alejandro'

#Usando el metodo set y pasandole el argumento que querramos podremos modificar la informacion del objeto
persona1.set_nombre('Alejandro')
#Si descomentamos la siguiente linea que llama al metodo privado podremos ver que no podemos llamar a dicho metodo
#por que esta privado
#persona1.__metodo_privado()

#Con el metodo get nos muestra el valor actualizado
print(persona1.get_nombre())
#Y mostramos el estado del objeto
print(persona1)

#Con los metodos setters and getters podemos acceder a la informacion del objeto para poder modificar la informacion
