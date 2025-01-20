"""
    Tambien podemos crear nuestras podrias expections para poder tratar los errores
"""
#Para ello creamos nuestra clase que heredara la informacion de Exception
class OperadorException(Exception):
    #Despues creamos el constructor que reciba el self y un mensaje
    def __init__(self, mensaje):
        #Despues con super y init mandamos el mensaje
        super().__init__(mensaje)
#De esa forma ya estamos creando nuestras excepciones

#Creamos la funcion de division
def division(a,b):
    #Dentro de un if preguntamos si b es 0
    if b == 0:
        #Si es asi, usamos la palabra reservada raise con el zerodisionerror y le pasamos un mensaje personalizado
        #Usando ahora nuestro OperadorException
        raise OperadorException('Error: No se puede dividir entre cero')
    #Si b no es igual a cero, realizamos la operacion normal
    else:
        return a / b

#Ahora si mandamos un cero
#Podremos ver que el mensaje de error es personalizado y muestra donde esta el error
a = division(4,0)
print(a)
#OperadorException: Error: No se puede dividir entre cero

#Nos muestra ese error que nos da a entender que ya estamos lanzando nuestras propias exceptions
