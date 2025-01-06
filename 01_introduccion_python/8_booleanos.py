#Hemos visto diferentes ejercicios que devuelven True y False
#Dichas palabras reservadas son del tipo booleano donde True = 1 y False = 0
print(type(True))
print(type(False))

#Como se menciona tiene un valor numerico entonces podemos hacer operaciones con ellos
a = True + True #Devuelve 2 ya que True vale 1
b = False * 10  #Devuelve 0 ya que False vale 
c = True * 5 #Devuelve 5 ya que True vale 1

print(a,b,c)

#Usando operadores relacionales
d = True > False #Devuelve True porque 1 > 0
e = True == False #Devuelve False por que 1 != 0
print(d,e)

#Usando operadores por asignacion
f = 0
f += True
f += True
f += True

print(f) #Devuelve 3

#Estos valores al ser tambien numericos son muy modificables y utiles para hacer diferentes aplicaciones
#O realizar comparaciones para una determinada accion
