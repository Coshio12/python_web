"""
    PRACTICA: PRIMALIDAD
    Crea un sistema que detecte si un numero es primo o no
    
    Para solucionar este problema se requiere que el usuario
    ingrese un numero por teclado y el sistema detexti si es primo o no
    
    Un numero es aquel que se puede dividir solo dos veces por 1 y por si misma
"""
#Primero definimos la funcion es_primo que recibe una palabra como parametro
def es_primo(numero):
    #Iniciamos un contador ya que tenemos que saber cuantas divisiones se hacen
    contador = 0
    
    #Creamos un for con un rango dado por el usuario
    #el metodo range recibe dos parametros el valor inicial del rango y el final, se suma +1 en el segundo parametro
    #para que pueda contar el numero que se ingresa por teclado
    for i in range(1,numero+1):
        #Este if verifica si el numero es 1 o si el valor i es igual al numero del usuario
        #Si es verdad continua al siguiente if
        if i == 1 or i == numero:
            continue
        
        #Verifica la cantidad de veces que el numero del usuario es divido con numeros entre rango
        #solamente si es posible
        if numero % i == 0:
            contador += 1
    
    #Este if verifica si el contador es igual a 0 es primero (true) y si es diferente a 0 no es primo (false)
    if contador == 0:
        return True
    else:
        return False
    
def main():
    #Pedimos el numero al usuario
    numero = int(input('Ingrese un numero: '))
    
    #verificamos en el if si la funcion con el numero del usuario pasado como parametro devuelve true o false
    #E imprimimos el resultado
    if es_primo(numero):
        print('Es primo')
    else:
        print('No es primo')

#Este if llama a la funcion main
if __name__ == '__main__':
    main()