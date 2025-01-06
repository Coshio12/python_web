"""
Practica 02: Calcular precio de venta
Enunciado: Dado el valor de venta de productos, hallar el IGV (18%) y el precio de venta
Analisis: Para la solucion de este problema, se requiere que el usuario ingrese el valor de venta del producto
y el sistema realice el calculo respectivo para hallar el IGV y el precio de venta, para esto use la expresion
igv = vv * 0.18
pv= vv+ igv

vv= valor de venta
"""
print('='*45)
print("Calculando el precio de venta")
print('='*45)

#Parte de entrada de datos
vv = float(input('Ingrese el valor de venta del producto: '))

#Calculos segun el analisis del enunciado
igv = vv * 0.18
pv = vv + igv

#Salida de datos segun las operaciones necesarias
print('='*45)
print('SALIDA DE DATOS')
print('='*45)
print('VALOR VENTA: ',vv)
print('IGV: ',igv)
print('PRECIO DE VENTA: ', pv)
print('='*45)
