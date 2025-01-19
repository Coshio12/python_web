from figuras import Rectangulo, Circulo, probar_figura

def main():
    while True:
        menu="""
AREA Y PERIMETRO DE FIGURAS GEOMETRICAS
 
    1 - Rectangulo
    2 - Circulo
    3 - Salir
    Ingrese una opcion
"""
        opcion = input(menu)
        if opcion == '1':
            # nombre = 'Rectangulo'
            base = float(input('Ingrese la base: '))
            altura = float(input('Ingrese la altura: '))
            figura = Rectangulo(base,altura)
            probar_figura(figura)
        elif opcion == '2':
            #nombre = 'Circulo'
            radio = float(input('Ingrese el radio: '))
            figura = Circulo(radio)
            probar_figura(figura)
        elif opcion == '3':
            print('Gracias por usar el programa, cerrando')
            break
        else:
            print('Opcion no valida, intente de nuevo')

if __name__ == '__main__':
    main()