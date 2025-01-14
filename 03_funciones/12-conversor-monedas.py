"""
    PRACTICA: CONVERSOR DE MONEDAS
    -Crea un siste,a que convierta de moneda nacional a dolares, ejenmplo se soles a dolares
    de peso mexicano a dolares, etc
    -Para solucionar este problema se requiere que el usuario ingrese la cantidad de monedas nacionales
    y luego realizar la conversion
    -Para este sistema debe hacer un menu de navegacion para seleccionar a que tipo de moneda se hara la conversion
    y tambien para cerrar el programa, el sistema no debe cerrarse si no lo deseas
"""
#Definimos la funcion de convertir la moneda que recibe de parametros el valor del dolar y el pais
def convertir(valor_dolar, pais):
    #Pide la cantidad que se desea convertir
    cantidad_moneda = float(input(f'Ingrese cantidad de {pais}: '))
    
    #Se realizan las operaciones necesarias
    dolar = cantidad_moneda / valor_dolar
    dolar = round(dolar,2)
    
    #Se imprime el valor final
    print(f'Tienes ${dolar} Dolares')
    
#Se desarrollo dos soluciones diferentes al sistema
#Usando metodos que se uso en anteriores ejercicios
#Y uno usando nuevos para poder demostrar que para el problema hay diferentes soluciones
def main():
    
    #Se crea bucle infinito con while
    while True:
        #Se imprime el menu
        print('='*45)
        print('Sistema de conversion de monedas')
        print('='*45)
        print('Cual es tu pais?\n 1.Bolivia\n 2.Argentina\n 3.Colombia\n 4.Mexico\n 5.Peru\n 6.Salir')
        print('='*45)
        #Se pide que el usuario digite una opcion
        opcion = int(input('Tu opcion es: '))
        print('='*45)
        #Se realiza una comparacion y por cada valor que elija el usuario realizara una conversion diferente
        #Segun el valor que haya digitado el usuario entre los valores 1 y 6
        #Para ello usamos la palabra reservada match y la opcion del usuario
        match opcion:
            #Cada caso se ejecutara segun el valor que haya elegido el usuario
            #Cada caso colocara la modena del pais y su valor dentro de la funcion creada y devolvera la conversion
            case 1:
                pais = 'Peso Boliviano'
                valor_dolar = 6.94
                convertir(valor_dolar,pais)
                print('='*45)
            case 2:
                pais = 'Peso Argentino'
                valor_dolar = 1037.34
                convertir(valor_dolar,pais)
                print('='*45)
            case 3:
                pais = 'Peso Colombiano'
                valor_dolar = 3471.27
                convertir(valor_dolar,pais)
                print('='*45)
            case 4:
                pais = 'Peso Mexicano'
                valor_dolar = 20
                convertir(valor_dolar,pais)
                print('='*45)
            case 5:
                pais = 'Sol Peruano'
                valor_dolar = 3.61
                convertir(valor_dolar,pais)
                print('='*45)
            #En este caso que es de cierre del programa
            #Se usara la palabra reservada break que hara que el programa se detenga imprimiendo el mensaje
            case 6:
                print('Gracias por usar este programa, cerrando')
                print('='*45)
                break
            #En este caso se coloca una barra baja para que cada opcion que se digite y no este en el menu
            #Imprimira un mensaje para que el usuario digite otro valor
            case _:
                print('Opcion invalida, digite de nuevo')
    
    #Se crea bucle infinito con while
    while True:
        #Se muestra el menu
        menu = """
        1.-Soles Peruanos a Dolares
        2.-Pesos Mexicanos a Dolares
        3.-Pesos Colombianos a Dolares
        4.-Salir
        Ingrese una opcion: 
        """
        #Se guarda la opcion del usuario
        opcion = input(menu)
        
        #Con diferentes metodos if, elif y else se realizara las comparaciones necesarias
        #tomar en cuentra que las comparaciones son con un caracter de texto no con un numero entero
        #Segun la opcion se pasa al metodo el valor del dolar del pais y la moneda
        if opcion == '1':
            convertir(3.61,'Soles Peruanos')
        elif opcion == '2':
            convertir(20,'Pesos Mexicamos')
        elif opcion == '3':
            convertir(3471.27,'Pesos Colombianos')
        elif opcion == '4':
            #Si se usa la palabra reservada break se cierra el sistema
            print('Cerrando conversor de monedas')
            break
        #Si se digita un valor distinto al menu imprime el mensaje
        else:
            print('Opcion no valida, ingresa otro valor')

#Punto de inicio de la aplicacion
if __name__ == '__main__':
    main()
        