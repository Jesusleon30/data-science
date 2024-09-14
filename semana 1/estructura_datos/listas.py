
# caso de uso
# Creando una aplicacion para gestionar alumnos en una escuela
# en el cual debemos almacenar informacion de los mismos
# Las cuales pueden ser sus notas, horarios, etc
#  - Una lista de alumnos, que esten registrados
#  - un diccionario que asocie el alumno con sus notas
#  - Una tupla que almacene el horario del alumno



# LISTA ([]) -  list()
# puedo asignar qualquier tipo de dato
# Estructura de datos Mutable osea que la lista puede crecer a lo largo del tiempo 
# Index - Posicion (n-1) es una posicion inicia siempre con zero

# mi_lista = [1, 2, 3, 'hola', True]
# print(f' Primer valor de la lista: {mi_lista[0]}')
# print(f' Quarto valor de la lista: {mi_lista[3]}')



personas = [ 'Alan', 'Cristian', 'Eduardo']
print(f'inicio -> {personas}')

personas[0] = 'Cristian'
personas[1] = 'Alan'
print(f'sostituir el orden -> {personas}')

# funciones 
# append -> con esta funcion puedo agregar un  valor a mi lista y por default sera al ultimmo (se añade al final)
personas.append('Daniel')
print(f'append -> {personas}')

# insert -> esto va agregar un valor a la lista, pero indicandole su indice

# tiene dos parametros (indice y el valor de agregar)
personas.insert(0, 'Jesus')
print(f'insert -> {personas}')

# extend -> unir dos listas
personas_nuevas = ["Fritz", "Hugo","Juan"]
personas.extend(personas_nuevas)
print(f'extend -> {personas}')

# remove - elimina un valor de la lista 
personas.remove('Daniel')
print(f'remove -> {personas}')

# pop -> eliminar un valor de la lista, mediante su indice
personas.pop(5)
print(f'pop -> {personas}')

# sort -> ordenar los valores de una lista (con numeros de menor a mayor y letras del alfabeto)
# reverse=False -> menor a mayor (no es necesario definirlo)
# reverse=True -> mayor a menor
# este trabaja por defcto con el parametro reverse=False pero no es necesario definirlo
personas.sort() # oppure personas.sort(reverse=False)
print(f'sort -> {personas}')

personas.sort(reverse=True) # si le decimos True lo hace de mayor a menor en este caso lo tenemos que especificar
print(f'sort -> {personas}')

# len -> cuenta los elementos de una secuencia (estructura de datos o string)
print(f'total de personas: {len(personas)}') 


    