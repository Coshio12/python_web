"""
    PRACTIA: JUEGO - ADIVINA EL NUMERO
    -Crea un juego donde el sistema genere un numero aleatorio y el jugador intente adivinar este numero
    -Para crear este juego ten en cuenta los siguientes datos:
        Dificil 5 vidas
        Intermedio 7 vidas
        Facil 10 vidas
    -De acuerdo como va intentado el juego le debe dar una pista si el numero es mas grande o mas pequeño
    -Tambien tiene que indicarle las vidas que le queda
"""
#Importamos random
import random
#Definimos la funcion del juego que recibira como parametro las vidas que elije el usuario
def jugar (vidas):
    #Generamos el numero random y creamos la variable del numero del usuario
    numero_random = random.randint(1,100) #Numero entre 1 y 100
    numero_elegido = None
    
    #Creamos un bucle que se ejecutara mientras el numero random sea diferente al numero elegido
    while numero_random != numero_elegido:
        print('='*45)
        numero_elegido = int(input('Ingrese un numero entre 1 y 100: '))
        print('='*45)
        
        #En esta parte creamos las pistas que le daremos al usuario
        #Y restaremos las vidas
        if numero_random < numero_elegido:
            print('Elige un numero mas pequeño')
            vidas -= 1
        elif numero_random > numero_elegido:
            print('Elige un numero mas grande')
            vidas -=1
        
        #Si las vidas son iguales a 0, el usuario perdio y se muestra el numero que tenia que adivinar
        if vidas == 0:
            print('GAME OVER')
            print(f'El numero era {numero_random}')
            print('='*45)
            break
        #Segun se va jugando se muestra las vidas que quedan
        print(f'Las vidas que te quedan son {vidas}')
    
    #Este if solamente se ejecutara cuando el usuario haya adivinado el numero
    if numero_elegido == numero_random:
        print('FELICIDADES GANASTE')
        print(f'El numero era {numero_random}')
        
#Ahora en la funcion main creamos el menu de las vidas del usuario      
def main():
    print('='*45)
    print('ADIVINA EL NUMERO')
    print('='*45)
    
    #Mostramos el menu de dificiltad
    while True:
        print('Selecciona la dificiltad')
        menu = """
1.Nivel Dificil (5 vidas)
2.Nivel Intermedio (7 vidas)
3.Nivel Facil (10 vidas)
4.Salir
"""
#Pedimos que el usuario seleccione una dificultad
        dificultad = input(menu)
        
        #Segun el numero que elija se le pasara como argumento a la funcion jugar
        if dificultad == '1':
            print('='*45)
            print('Elegiste el nivel Dificil')
            vidas = 5
            jugar(vidas)
        elif dificultad =='2':
            print('='*45)
            print('Elegiste el nivel Intermedio')
            vidas = 7
            jugar(vidas)
        elif dificultad =='3':
            print('='*45)
            print('Elegiste el nivel Facil')
            vidas = 10
            jugar(vidas)
        elif dificultad == '4':
            print('='*45)
            print('Cerrando juego')
            print('='*45)
            break
        else:
            print('Opcion no valida, pruebe de nuevo')
    
#Punto de inicio de la aplicacion:
if __name__ == '__main__':
    main()
