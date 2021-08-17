###
# 1) Define una variable edad y asignale un valor entero.
#  Muestre su valor por pantalla.
#  Defina otra variable edad_cadena que contenga el valor de edad como una cadena de caracteres.
#  Comprueba el tipo de la nueva variable.
#  Utiliza la variable edad que has definido previamente y calcula la edad que tendría esa persona en el año 2035. 
###

edad=33
print(edad)
edad_cadena=str(edad)
#print(edad_cadena)
print(type(edad_cadena))
edad_2035=(2035-2021)+edad
print(edad_2035)

###
# 2) Al realizar una consulta en un registo hemos recibido unos valores corruptos. Al parecer entrega el nombre y apellido del alumno al reves.
#  ¿que puede hacer para obtener el siguiente mensaje por pantalla?
###

cadena="azebaC ellehciM , 01"
cadena_volteada=cadena[::-1] # los corchetes indican indexacion, los dos puntos seguidos significa que va a tomar todos los valores dentro, el -1 arranca de atras para adealnte
print(cadena_volteada)

print(cadena_volteada[4::], "ha sacado un ",cadena_volteada[:2])
