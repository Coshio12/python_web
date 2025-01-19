#Importamos las clases desde persona
from persona import Persona, Atleta, Ciclista

#Creamos el objeto persona
persona = Persona('Alejandro')
persona.moverse()

#Creamos el objeto atleta
atleta = Atleta('Jose')
atleta.moverse()

#Creamos el objeto ciclista
ciclista = Ciclista('Viktor')
ciclista.moverse()

#Como podemos observar cambiamos la funcionalidad del metodo padre en los hijos
#Pero no perjudica el funcionamiento de los archivos cumpliendo el polimorfismo
