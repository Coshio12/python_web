"""
    Aplicando lo aprendido en esta seccion, intenta resolver el siguiente problema
    antes de ver el codigo final
    
    Enunciado:Un restaurante ofrece un descuento del 10% para consumos de hasta 100 soles y un 
    descuento del 20% para consumos mayores, para ambos casos se aplica un impuesto del 19%. 
    Determinar el monto del descuento, el monto del impuesto y el total a pagar 
    por el consumo de un cliente.
    Analisis: Se requiere que el usuario ingrese el monto del consumo 
    y el sistema verifica y caulcula el monto del descuento, el impuesto y el importe a pagar.
"""
# Definir variables y otros
print("Ingrese el monto de consumo:")
consumo = float(input('Consumo: '))
# Proceso
if consumo <= 100:
    dato_descuento = '10%'
    descuento = consumo *0.10
else:
    dato_descuento = '20%'
    descuento = consumo *0.20

monto_descuento = consumo - descuento
impuesto = monto_descuento * 0.19
total_pagar = monto_descuento + impuesto
# Datos de salida
print('='*31)
print('------------FACTURA------------')
print('='*31)
print('Descuento aplicado:', dato_descuento)
print('Monto de descuento:', descuento)
print('Monto de consumo:', consumo)
print('Monto con dscuento:', monto_descuento)
print('Impuesto:', impuesto)
print('Total a pagar:', total_pagar)
print('='*31)
