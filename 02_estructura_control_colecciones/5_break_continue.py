"""
    Las palabras reservadas break y continue
    break = Es aquella que termina un bucle, se lo puede colocar en cualquier parte del codigo
    provocando que la aplicacion se termine o salte a otra operacion
    continue = Sirve para seguir con la aplicacion si es que se termino en un determinado punto
"""

#Ejemplo con el break
#Crearemos una aplicacion con while de la manera tradicional
C = 0

while C < 10: #se ejucatara el codigo mientras C sea menor que 10
    C += 1 #C ira aumentando de valor 1 a 1
    print(C)
    #El siguiente if detectara que C vale 5
    #Y por accion del break terminara el bucle
    if C == 5: 
        print('Termino el bucle en: ', C)
        break
else:
    print('Fin de while')

#Ejemplo con el continue
C = 0
#Crearemos una aplicacion con while de la manera tradicional
while C < 10: #se ejucatara el codigo mientras C sea menor que 10
    C += 1 #C ira aumentando de valor 1 a 1
    print(C)
    #El siguiente if detectara que C vale 5
    #Y por accion del continue seguira ejecutando la aplicacion con normalidad
    #pero cuando C sea 6 no se volvera a ejecutar el if
    if C == 5:
        print('Saltar de iteracion')
        continue
    print("Despues de continue")
else:
    print('Fin de while')
