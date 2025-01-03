entrada = input('Cual es el precio de adquisicion?')

precio = int(entrada)

igv = precio * 0.18

pv = precio + igv

print(f'El precio de adquisicion es {precio} Bs.')
print(f'El igv = {igv}')
print(f'El precio de venta es: {pv}')