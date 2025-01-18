#Importamos el paquete con un script es especifico y le damos un alisas "a"
import my_paquete.aritmetica as a

#Definimos la funcion main que llamara a los metodos para crear una aplicacion
def main():
    #Suma de n numeros
    suma = a.sumar(4,4,5,8,7,9)
    #Resta de dos numeros
    resta = a.restar(10,5)
    #Potencia
    potencia = a.potencia(3,3)
    
    print(f'La suma es: {suma}')
    print('La resta es: ',resta)
    print('La potencia es: ',potencia)

#Entrypoint para llamar a main
if __name__ == '__main__':
    main()