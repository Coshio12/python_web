"""
    Aplicando lo aprendido en esta seccion, intenta resolver el siguiente problema
    antes de ver el codigo final
    
    Enunciado: Debido a los excelentes resultados, el restaurante decide ampliar sus ofertas
    de acuerdo a la siguiente escala de consumo. Determinar el monto de descuento, impuesto y total
    -----------------------------
    |Consumo S/   | Descuento % |
    -----------------------------
    |Hasta 100    |     10      |
    |Mayor a 100  |     20      |
    |Mayor a 200  |     30      |
    -----------------------------
    Analisis: Para la solucion de este problema, se requiere que el usuario ingrese el consumo
    y el sistema verifica y calcula el monto del descuentto, impuesto y el importe total
"""
print('Restaurante Familiar')
consumo = float(input('Ingrese el consumo total: '))
valor_descuento = ''
monto_descontado = 0

if consumo > 0:
    if consumo <= 100: #0-100
        valor_descuento = '10%'
        descuento = 0.1
        monto_descontado = consumo * descuento
    elif (consumo>100) and (consumo<=200): #100 - 200
        valor_descuento = '20%'
        descuento = 0.2
        monto_descontado = consumo * descuento
    elif (consumo>200): #201- infinito
        valor_descuento = '30%'
        descuento = 0.3
        monto_descontado = consumo * descuento

    consumo_descuento = consumo - monto_descontado
    impuesto = consumo_descuento * 0.19
    total_pagar = consumo_descuento + impuesto

    print('='*45)
    print('-------------------FACTURA-------------------')
    print('='*45)
    print('Consumo: ',consumo)
    print('Descuento: ',valor_descuento)
    print('Monto descontando: ',monto_descontado)
    print('Consumo con descuento: ',consumo_descuento)
    print('Impuesto: ', impuesto)
    print('Total a pagar: ',total_pagar)
    print('='*45)
else:
    print('Error al ingresar el consumo')
