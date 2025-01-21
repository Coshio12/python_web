"""
    Tambien podemos manejar archivos en python, como ser txt entre otros
    esto lo podemos lograr importando una libreria
"""
#Desde io importamos open
from io import open

from os import path

#Creamos una funcion
def escibir_archivo():
    #Creamos una variable llamando a open y pasandole como argumento, el nombre del archivo y como se abrira
    #Estamos pasando un archivo que se llamara "texto" con extension .txt y abriendo en modo escritura
    #Si el archivo no existe, se creara un archivo .txt con el nombre indicado
    archivo = open('texto.txt','w')
    #no se guarda, se reescribe
    #Despues desde la variable llamamos al metodo write y  le pasamos el mensaje
    #NOTA: Si hay un texto ya en el archivo, esta linea reemplazara el texto que esta en el archivo por 
    #el texto que le pasaremos en la linea de codigo
    archivo.write('Hola Mundo desde vs code')
    #Y tenemos que cerrar el flujo de trabajo de la funcion
    archivo.close()
#Llamamos a la funcion 
#escibir_archivo() #Descomenta esta linea
#Si abrimos el archivo veremos que lleva el mismo nombre que le indicamos que se cree
#Y con el mismo contenido que le pasamos

"""
    Asi como podemos escribir dentro de un archivo tambien podemos leer la informacion de un archivo
    Antes realice un cambio en el texto.txt desde el propio texto agregandole una frase
    Y para la lectura necesitaremos path de os que esta importamos desde mas antes
"""
#Creamos la funcion leer_archivo
def leer_archivo():
    #Preguntamos con path si el archivo existe
    if path.isfile('texto.txt'):
        #Si existe lo abriremos con el modo lectura
        archivo = open('texto.txt','r')
        #La siguiente linea de codigo es si queremos leer toda la informacion del texto con el metodo read
        #textos = archivo.read() 
        #Tambien existe otros metodos como ser readline que devolvera solo la primera linea de texto
        #Y readlines que devolvera todas las lineas de texto en una lista
        textos = archivo.readlines()
        #Siempre que abrimos un archivo debemos cerrar el flujo
        archivo.close()
        print(textos)
    
    #Si no existe el archivo devolvera el siguiente mensaje
    else:
        print('No existe el archivo')
#Llamamos a la funcion
#Descomenta la siguiente linea para ver el funcionamiento
#leer_archivo()

#Tambien podemos agregar informacion al archivo
#Creamos la funcion de agregar datos
def agregar_datos():
    #Preguntamos con path si el archivo existe
    if path.isfile('texto.txt'):
        #Si existe lo abriremos con el modo actualizar datos
        archivo = open('texto.txt','a')
        #Y con write agregamos la informacion que querramos
        archivo.write('\nHola Jose')
        
        #Siempre que abrimos un archivo debemos cerrar el flujo
        archivo.close()
    
    #Si no existe el archivo devolvera el siguiente mensaje
    else:
        print('No existe el archivo')
    
#Llamamos a la funcion
#Descomenta la siguiente linea de codigo
#agregar_datos()

#Creamos la funcion modificar_datos
def modificar_datos():
    #Preguntamos con path si el archivo existe
    if path.isfile('texto.txt'):
        #Abrimos el archivo en modo lectura y escritura
        archivo = open('texto.txt','r+')
        #Guardamos toda la informacion en una lista
        textos = archivo.readlines()
        #Imprimimos en primera instancia
        print(textos)
        
        #Modificamos un valor de la lista
        textos[1] = 'Hola Jose Alejandro\n'
        #Vemos el resultado
        print(textos)
        
        #Agregamos el puntero para realizar la modificacion el punto cero es el inicio
        archivo.seek(0)
        
        #Desde el inicio reescribimos todo el archivo con la informacion de esta funcion
        archivo.writelines(textos)
        
        #Cerramos el flujo de trabajo
        archivo.close()
        print(textos)
    #Si no existe el archivo devolvera el siguiente mensaje
    else:
        print('No existe el archivo')

#Llamamos al metodo modificar datos     
#Descomenta la siguiente linea de codigo   
#modificar_datos()

#Tambien podemos eliminar datos que estan dentro de un archivo con la logica de abrir en modo escritura
#Creamos la funcion
def eliminar_datos():
    #abrimos el archivo en modo escritura
    archivo = open('texto.txt', 'w')
    #esto borrara la informacion dentro del archivo
    #Cerramos el flujo
    archivo.close()
    
#Llamamos al metodo eliminar datos
eliminar_datos()

#De esta manera podemos manejar los archivos en python
