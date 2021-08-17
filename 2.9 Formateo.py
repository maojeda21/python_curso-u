# Formateo: ser refiere a la propiedad de las cadenas de textos que tienen de permitirnos dejar espacios donde al final vamos a definir que valores 
# van a aparecer dentro de estos espacios.

print('{} es el primer valor y {} es el segundo'.format(1,2))

print('En este caso alteramos el orden y el {1} aparece primero, luego el {0}'.format('Uno','Dos'))

nombre='la cartuja de parma'
x=.7
print(f'El valor de {nombre} es',x) # al colocar una "f/F" delante de la cadena podemos formatear la variable declarando el nombre, sino imprimiría literal {nombre}.

# Tambien podemos aplicar a métodos.
print(f'El valor de {nombre.title()}\n es', x ,'dolares por papel')

diccionario={'uno':x,'dos':x.__add__(10)}
print(diccionario)

print(f'{nombre.title()} cuesta {diccionario["uno"]} pesos \n y el otro libro {diccionario["dos"]} pesos')
