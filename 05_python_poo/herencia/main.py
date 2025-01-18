"""
    Ahora vamos a entender que es herencia
    Segun la propia herencia, se trata de usar o extraer los atributes de una clase padre
    Es decir que podremos usar atributos de otra clase desde un objeto distinto
    
    Ir a persona.py
"""
#Importamos no clase padre Persona, si no la sub-clase o clase hijo que es Cliente
from persona import Cliente

#Construimos el objeto
cliente1 = Cliente('Jose','Cossio')
#Mostramos la informacion
cliente1.detalle_persona()

#Creamos otro objeto
cliente2 = Cliente('Alejandro', 'Vidaurre')
#Mostramos el estado del objeto
print(cliente2)

#Como podemos ver en la clase cliente no se hizo nada pero
#pudimos acceder a las variables de la clase padre para poder mostrar la informacion
#es decir, la clase cliente heredo los atributos y metodos de la clase Persona
