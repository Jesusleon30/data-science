
# AND (y), si ambas condiciones devuelve un true, el resultado final es true
a = 5 
b = 10
print(f'AND: {a > 3 and b < 10}')
# basta que uno sea false y el resultado final es false


# or ( o ), basta que una condicion devulva true, para que el resultado final sea true
c = 7
d = 9 
print(f'OR: {c < 5 or d > 7}')

# NOT (no), invertir el valor verdadero
e = 10 
print(f'NOT: {not e == 11}') # esto va a iinvertir el valor de false a true

# otro ejemplo de not
a = 5 
b = 10
print(f'AND: {a > 3 and not b < 10}')
