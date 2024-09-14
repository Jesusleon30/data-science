

# no cambian para nada una vez declarada
#  estos son los unicos momentos a los qual se usan



# tuplas ()
# indice (n - 1)

# ejemplo dias de semana que nunca va a cambiar  
dias_semana =("Lunes", "Martes", "Miercoles", "Jueves", 
              "Viernes", "Sabado", "Domingo")

print(dias_semana[6])

# index - retorna el indice del valor
indice_martes = dias_semana.index('Martes')
print(f'index->{indice_martes}') 

# count -> retorna las veces que existe un valor 
miercoles_contador = dias_semana.count('Mercoles')
print(f'count -> {miercoles_contador}')


################################################
print(f'inicio -> {type(dias_semana)}')
dias_semana_lista = list(dias_semana)
print(f'casteo -> {type(dias_semana_lista)}')

dias_semana_lista.append('Otros')
print(f'append -> {dias_semana_lista}')

dias_semana = tuple(dias_semana_lista)
print(f'casteo -> {type(dias_semana)}')
print(f'tupla -> {dias_semana}')
