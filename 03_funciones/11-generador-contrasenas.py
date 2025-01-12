"""
    PRACTICA: GENERADOR DE CONTRASEÑAS
    -Crear un sistema que genere una contraseña aleatoria
    
    -Se requiere de listas, listas en mayusculas, minusculas, lista de numeros, 
    listas de simbolos y luego armar una contraseña aleatoria sacando caracteres de estas listas
"""
#Al pedir que se necesita una contraseña aleatoria necesitaremos la libreria de random asi que la importamos
import random

#Creamos la funcion de generar contraseña
def generar_contrasena():
    #El problema pide crear listas de caracteres en especifico asi que las creamos
    mayusculas = ['A','L','E','J','N','D','R','O','J','S']
    minusculas = ['c','o','s','v','i','d','a','u','r','e']
    simbolos = ['!','#','$','%','&','/','-','_','?','¡']
    numeros = ['1','2','3','4','5','6','7','8','9','0']

    #Necesitamos que todas estas listas esten en una sola variable asi que las unimos todas
    caracteres = mayusculas + minusculas + simbolos + numeros
    
    #Y creamos la variable contraseña que sera una lista vacia donde se guardara la contraseña
    contrasena = []
    
    #creamos un for donde recorrera hasta el rango que nosotros querramos
    #En este caso sera una contraseña de 15 caracteres
    for i in range(15):
        #creamos la variable caracteres random y con uno de los metodos de la libreria que es choice
        #Seleccionara un caracter de la lista de manera aleatoria
        caracteres_random = random.choice(caracteres)
        
        #Entonces una vez seleccionado el caracter lo guardamos con el metodo append en la lista vacia que creamos
        contrasena.append(caracteres_random)
    
    #Despues esa lista que ya no esta vacia tiene los datos asi: contrasena=['a','#',....]
    #Entonces tenemos que convertir esa lista en una cadena de caracteres
    #Para eso esta el metodo join
    contrasena = "".join(contrasena)
    
    #Y retornamos la contraseña generada
    return contrasena

#En la funcion main colocamos como queremos que imprima el resultado
def main():
    #generamos la contraseña llamando a la funcion
    contrasena = generar_contrasena()
    
    #Y la imprimimos
    print(f'La contraseña es: {contrasena}')

if __name__ == '__main__':
    main()
