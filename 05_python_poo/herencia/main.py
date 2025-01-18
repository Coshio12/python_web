"""
    Ahora vamos a entender que es herencia
    Segun la propia herencia, se trata de usar o extraer los atributes de una clase padre
    Es decir que podremos usar atributos de otra clase desde un objeto distinto
    
    Ir a persona.py
"""
#Importamos no clase padre Persona, si no la sub-clase o clase hijo que es Cliente
#Para poder usar nuevos metodos acerca de la herencia debemos importar de la clase persona el objeto empleado
from persona import Cliente, Empleado

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

#Ahora si queremos aumentar mas cosas a los metodos heredados hay que hacer lo siguiente
#ir a persona.py y despues volver
print('='*45)
#Creamos dos objetos empleados
#Desde aqui ya notamos que tenemos que agregar otro argumento para poder llamar a la funcion
empleado1 = Empleado('David','Cruz',2500)
empleado2 = Empleado('Samir','Uño',4500)

#Para hacer la prueba llamamos al metodo de detalle persona
empleado1.detalle_persona()
print('='*45)
#Llamamos al metodo detalle_empleado
empleado1.detalle_empleado()
print('='*45)
#Y imrpimimos el estado del empleadp2
print(empleado2)

#Podemos notar que el detalle_persona solo imprime los datos heredados, es decir, los atributos de la clase padre
#En cambio si vemos lo que devuelve detalle_empleado podemos notar como agrega el sueldo del empleado
#Y lo mismo pasa al momento de mostrar el estado del objeto2
