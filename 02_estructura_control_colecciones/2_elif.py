#Se puede dar el caso que en una de nuestras aplicaciones
#Se tengan que realizar diferentes acciones
#Y para no tener que llenar la aplicacion de muchos if y else
#Existe la palabra reservada "elif"
#Que nos permite realizar multiples condiciones

#Ejemplo
vocal = input('Ingrese un caracter: ')#Pide un caracter al usuario

if vocal == 'a' or vocal == 'A': #Se realiza una comparacion normal
    print(vocal, 'ES VOCAL')
elif vocal == 'e' or vocal == 'E': #Elif funciona como un else pero con la posibilidad de realizar condiciones
    print(vocal, 'ES VOCAL')
elif vocal == 'i' or vocal == 'I':
    print(vocal, 'ES VOCAL')
elif vocal == 'o' or vocal == 'O':
    print(vocal, 'ES VOCAL')
elif vocal == 'u' or vocal == 'U':
    print(vocal, 'ES VOCAL')
else: #Y al final siempre un else para ejecutar una accion cuando
# no se va a realizar ninguna operacion que nosotros necesitemos
    print(vocal, 'NO ES VOCAL')
