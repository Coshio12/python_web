"""
    PRACTICA: CONVERSOR DE MONEDAS
    -Crea un siste,a que convierta de moneda nacional a dolares, ejenmplo se soles a dolares
    de peso mexicano a dolares, etc
    -Para solucionar este problema se requiere que el usuario ingrese la cantidad de monedas nacionales
    y luego realizar la conversion
    -Para este sistema debe hacer un menu de navegacion para seleccionar a que tipo de moneda se hara la conversion
    y tambien para cerrar el programa, el sistema no debe cerrarse si no lo deseas
"""
def convertir(valor_dolar, pais):
    cantidad_moneda = float(input(f'Ingrese cantidad de {pais}: '))
    
    dolar = cantidad_moneda / valor_dolar
    dolar = round(dolar,2)
    
    print(f'Tienes ${dolar} Dolares')
    
    
def main():
    a = True
    while a!=False:
        print('='*45)
        print('Sistema de conversion de monedas')
        print('='*45)
        valor = int(input('Cual es tu pais?\n1.Bolivia\n2.Argentina\n3.Salir\n'))
        match valor:
            case 1:
                pais = 'peso boliviano'
                valor_dolar = 6.94
                convertir(valor_dolar,pais)
                print('='*45)
            case 2:
                pais = 'peso argentino'
                valor_dolar = 1037.34
                convertir(valor_dolar,pais)
                print('='*45)
            case 3:
                print('Gracias por usar este programa')
                print('='*45)
                a = False

if __name__ == '__main__':
    main()
        