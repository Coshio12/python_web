#Hay una formas de mandar datos a sun script
#Y es de la misma manera que ejecutas un codigo de python
#Para ello importaremos sys
import sys

#Usaremos uno de sus metodos que es argv que segun los valores que se le pasan
#Mueve todo a una lista
#Este if verifica que la lista sea de tamaño 3 para poder ejecutarse si no es asi, devolvera un mensaje de error
if len(sys.argv) == 3:
    #Esta variable con el metodo argv[1] detecta el texto que se le pasara
    #NOTA: El texto debe estar entre comillas ("") para que la consola detecte que es un texto
    texto = sys.argv[1]
    #Esta variable guarda el valor de un numero
    #Este metodo sys.argv guarda la informacion como caracter, entonces hay que volverlo entero
    cantidad = int(sys.argv[2])

    #Creamos un contador
    c = 0
    #Este bucle mientras el contador sea menor a la cantidad imprimira el texto que se le paso
    while c<cantidad:
        print(texto) 
        #Y aumentara el contador
        c += 1
else:
    print('Error, ingresa los argumentos correctamente')
    print('Ejemplo: entra_script.py "Texto" 5')