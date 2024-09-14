

# String , te busca en especifico lo que le pides 

texto = "Python es practico"
# in -> si existe el valor dentro de la secuencia
print(f'Pertenencia - String: {"Python" in texto}') # mayuscula
# te da TRUE

texto = "Python es practico"
print(f'Pertenencia - String: {"python" in texto}') # minuscula
# te da FALSE


texto = "Python es practico"
print(f'Pertenencia - String: {"python" in texto.lower()}') # trasforma en minuscula todo

texto = "Python es practico"
print(f'Pertenencia - String: {"python" in texto.upper()}') # trasforma en mayuscula todo

texto = "Python es practico"
# in -> si existe el valor dentro de la secuencia
print(f'Pertenencia In - String: {"Python" in texto}')

# not in -> si no existe  el valor dentro de la secuencia
print(f'Pertenencia Not In - String: {"Java" not in texto}')



# lista falta escrivir
mi_lista = [ 1, 2, 3, 5]
print(f'Pertenencia In - Lista: {2 in mi_lista}')
print(f'Pertenencia Not In - Lista: {6 not in mi_lista}')
