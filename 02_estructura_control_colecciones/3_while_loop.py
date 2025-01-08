"""
    El bucle while es aquella palabra reservada que 
    ejecuta distintas operaciones dentro del bucle
    Es importante tener cuidado con la condicion porque podemos provocar un bucle infinito
"""
c = 0
while c < 10: #se ejecutara el bucle mientras c sea menor a 10
    c += 1 #la variable c iran aumentando de 1 en 1
    print("bucle", c)

#Ingresaremos un numero y que sume sus anteriores numeros es decir
#Usuario digito 5, la operacion deberia ser 1+2+3+4 = 10

n = int(input('Ingrese un numero: '))    

suma = 0 #variable para guardar la suma
menores_n = 0 #variable de incremento

while menores_n < n: #se ejecutara el codigo mientras menoress_n sea menor que n
    suma += menores_n #la variable seguira sumando su valor mas el valor del contador
    menores_n += 1 #el contador ira aumentando
print('La suma es: ',suma)
    