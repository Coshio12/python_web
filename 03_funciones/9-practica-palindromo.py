"""
    PRACTICA
    Crear un sistema que detrecte si una palabra es laindroma o no
    
    Para solucionar este problema el usuario tiene que ingresar por pantalla
    una palabra y el sistema verificara si es palindromo o no
    
    Una palabra palindroma se lee de igual forma como de la derecha y de la izquierda
"""
#Apartir de ahora ejecutaremos las funciones dentro de un entry point que seria la funcion principal
#Ya preparandonos para crear aplicaciones mas grandes
#Definimos la funcion palindromo que recibe una palabra
def palindromo(palabra):
    #El usuario puede dijgitar una palabra de distintas maneras, ya sea con espacios, mayusculas o minusculas
    #Entonces preveendo eso modificaremos la palabra de entrada para que siempre funcione el sistema
    #Primero reemplazamos los espacios en blanco con replace
    palabra = palabra.replace(' ','')
    #Despues hacemos que toda la palabra este en minuscula con lower
    palabra = palabra.lower()
    
    #creamos la variable de palabra invertida y con slicing hacemos que se invierta la palabra
    palabra_invertida = palabra[::-1]
    
    #creamos un if para comprobar si la palabra es palindroma o no, haciendo que el if
    #Devuelva valores booleanos
    if palabra == palabra_invertida:
        return True
    else:
        return False

#Entry point y una funcion principal
#Apartir de aqui creamos la funcion main donde iran los prints u otras operaciones
def main():
    #Pedimos la palabra al usuario
    palabra = input('Coloque una palabra una palabra: ')
    
    #mandamos la palabra a la funcion
    es_palindroma = palindromo(palabra)
    
    #con el if comprobamos si la funcion devuelve true o false que es lo que esperamos
    #y imprime si la palabra es palindroma o no
    if es_palindroma:
        print('Es palindromo')
    else:
        print('No es palindromo')

#Entrypoint de una aplicacion
#Punto de entrada de la aplicacion
#se llama la funcion principal main con este if
if __name__ == '__main__':
    main()
