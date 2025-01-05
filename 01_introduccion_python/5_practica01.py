"""
    Practica 01: Calcular el cociente y residuo
    Enunciado: Hallar el cociente y el residuo de dos numeros enteros
    Analisis: Para la solucion el usuario debe ingresar dos numeros enteros y el sistema realice el calculo respectivo
"""

print("Calculando el cociente y el residuo")
divisor = int(input('Ingrese el divisor entero: '))
dividendo = int(input('Ingrese el dividendo: '))

cociente = divisor/dividendo
residuo = divisor % dividendo

print(f"El cociente es: {cociente} \nEl residuo es: {residuo}")
