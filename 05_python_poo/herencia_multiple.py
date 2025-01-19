"""
    En python tambien se puede crear una sub-clase que tenga informacion de dos clases padre
    A esto se le llama herencia multiple
    Una de las caracteristicas de esta herencia es que python dara mas importancia al primer argumento que se le pase
    Es decir importa mucho los parametros por posicion
"""
#Creamos una clase padre
class A:
    #Creamos un constructor que solo devuelve un mensaje
    def __init__(self):
        print('Soy la clase A')
    
    #Creamos un metodo en la clase padre
    def a(self):
        print('Soy Metodo de A')

#Creamos una clase padre 
class B:
    #Creamos un constructor que solo devuelve un mensaje
    def __init__(self):
        print('Soy la clase B')
    
    #Creamos un metodo en la clase padre
    def b(self):
        print('Soy Metodo de B')
        
#le da mas importancia al primero
#Creamos una clase hijo que hereda la informacion de dos clases padre
class C(A,B):
    #No creamos un constructor pero si un metodo propio
    def c(self):
        print('Soy metodo de C')

#Desde aqui creamos los objetos
#Creamos un objeto de c
c1 = C()
#Vemos que sin pasarle argumentos devuelve el metodo de la clase A ya que es la primera que hereda

#Pero tambien podemos acceder a los metodos de la otra clase padre del cual hereda su metodo
c1.b()

#Tambien puede usar el propio metodo que esta en la clase c
c1.c()

#Asi funciona la herencia multiple
