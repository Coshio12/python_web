"""
    Otro de los modulos mas usados es el modulo datatime
    Este modulo sirve para poder usar la fecha
    
    Es un modulo bastante util para crear calentadrios, registros entre otros
"""
#Desde datatime importamos datatime y le damos el alias "d"
from datetime import datetime as d

#now nos muestra el valor de la fecha actual
#varia segun el momento que ejecutes el script
print(d.now())

#guardamos el valor que nos devolvio now en una variable
dt = d.now()

#dt.year nos muestra el valor del año de la variable
print(dt.year)

#dt.year nos muestra el valor del mes de la variable
print(dt.month)

#dt.year nos muestra el valor del dia de la variable
print(dt.day)

#dt.year nos muestra el valor de la hora de la variable
print(dt.hour)

#dt.year nos muestra el valor del minuto de la variable
print(dt.minute)

#dt.year nos muestra el valor del segundo de la variable
print(dt.second)

#dt.year nos muestra el valor del microsegundo de la variable
print(dt.microsecond)
