"""
    Dentro de los errores si no queremos usar el try except
    podemos usar la palabra reservada raise que funciona de la misma manera
"""
#Creamos una funcion division que recibe a y b
def division(a,b):
    #Dentro de un if preguntamos si b es 0
    if b == 0:
        #Si es asi, usamos la palabra reservada raise con el zerodisionerror y le pasamos un mensaje personalizado
        raise ZeroDivisionError('Error: No se puede dividir entre cero')
    #Si b no es igual a cero, realizamos la operacion normal
    else:
        return a / b

#Ahora si mandamos un cero
#Podremos ver que el mensaje de error es personalizado y muestra donde esta el error
a = division(4,0)
print(a)
