"""
    Una de las funciones que suelen ser utilziadas en aplicaciones mas grandes son las funciones recursivas
    
    Es una función que se llama a sí misma para resolver un problema, dividiéndolo en 
    problemas más pequeños hasta llegar a un caso base (la condición que detiene la recursión).
"""
#Creamos una funcion normal que recibe un numero entero como parametro
def factorial(numero):
    #print('valor inicion => ',numero) #Este print es para ver como se comporta el numero recibido al iniciar la funcion
    if numero >1:
        #Buscamos un factorial entonces tenemos que multiplicar el valor recibido por el valor anterior (n-1)
        numero = numero * factorial(numero-1)
    #print('valor final => ',numero) #Este print es para ver como se comporta la variable final
    return numero

n = int(input('Ingresa un numero entero: '))

f = factorial(n)
print(f'El factorial de {n} es: {f} ')
"""
Primera llamada:
    factorial(3)
        ¿3 > 1? Sí.
    Entonces calcula:
        3 x factorial(2)
    (¡Pausa! Necesitamos el resultado de factorial(2) antes de continuar.)
Segunda llamada:
    factorial(2)
    ¿2 > 1? Sí.
    Entonces calcula:
    2 x factorial(1)
    (¡Pausa! Necesitamos el resultado de factorial(1) antes de continuar.)
Tercera llamada:
    factorial(1)
    ¿1 > 1? No. Este es el caso base.
    Devuelve 1.
    
Regresando en la recursión:
Ahora que sabemos que factorial(1) = 1, volvemos hacia atrás:

En la segunda llamada (factorial(2)):
2x1=2
Devuelve 2.

En la primera llamada (factorial(3)):
3x2=6
Devuelve 6.
Resultado final:
La función termina y devuelve el valor 6.
"""
