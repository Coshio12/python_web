#Hasta ahroa estamos interactuando con el lenguaje de python
#ahora crearemos una pequeña aplicacion que funcione y que la consola pida la informacion para devolver un resultado
print("Suma de dos numeros enteros")

#Entrada de datos
#El metodo input lo que hace dentro de la consola la aplicacion se detiene para que el usuario pueda digitar el valor
#y al darle enter pasa a la siguiente linea de codigo y asi sucesivamente
numero_1 = input('Ingrese el primer numero: ')
numero_2 = input('Ingrese el segundo numero: ')
#pero al mostrar el resultado nos muestra un valor distinto a una suma comun y corriente
resultado = numero_1 + numero_2
#debido a que el input guarda los datos con el tipo str (string o cadena de texto)
print(type(numero_1), type(numero_2))

#Para ello debemos encerrar todo el input con el metodo int para que se guarde como valor numerico y asi mostrar el resultado de la suma
#esa logia se lo conoce como casting de datos
numero_1 = int(input('Ingrese el primer numero: '))
numero_2 = int(input('Ingrese el segundo numero: '))

#Realizando una suma
resultado = numero_1 + numero_2

#Salida de datos
print(f'El resultado es: {resultado}')
