# operador de salida (print)
nombres = "jesus"
# print(nombres)



# operadores matematicos (Aritmeticos)

# suma (+)
numero_1 = 10
numero_2 = 5
suma =  numero_1 + numero_2
# print(suma)

# concatenacion 
# la suma de 10 y 5 es: 15

# concatenacion larga
#print("la suma de" + " " + str(numero_1) )
print("la suma de " + str(numero_1) + " y " + str(numero_2) + " es: " + str(suma) )


# concatenar de modo simple
# f-string  # function de string
print(f'La suma de {numero_1} y {numero_2} es: {suma}')




# resta(-)
numero_3 = 5
numero_4 = 2
resta = (numero_3 - numero_4)
# print(resta)
print(f'La resta de {numero_3} y {numero_4} es: {resta}')


# multiplicacion(*)
numero_5 = 5
numero_6 = 10
multiplicacion = numero_5 * numero_6 
# print(multiplicacion)
print(f'La multiplicacion de {numero_5} y {numero_6} es: {multiplicacion}')


# potencias(**)
numero_7 = 3
potencia_al_cubo = numero_7 ** 3
# print(potencia_al_cubo) 
#print(3**3)
print(f'La potencia_al_cubo de {numero_7} y {numero_7} es: {potencia_al_cubo}')


# Residuo (%)
numero_8 = 24
numero_9 = 7
residuo = numero_8 % numero_9
# print(residuo)
print(f"el residuo de {numero_8} y {numero_9} es: {residuo}")

# Division entera (/) -> flotante (Decimal)
numero_10 = 15
numero_11 = 3
division = numero_10 / numero_11
# print(division) #float
print(f"la division entera de {numero_10} y {numero_11} es: {division}")

# division exacta (//) -> redondear hacia abajo
division_exacta = numero_10 // numero_11
# print(division_exacta) #entero
print(f"la division_exacta entera de {numero_10} y {numero_11} es: {division_exacta}")

# operador asignacion
# igual (=)
x = 10
print(x)
print(f"el valor de x es: {x}")

# incremento (+=)
x += 2  # x = x + 2
print(x)
print(f'el valor de x por 2 es: {x}')

# reducir(-=)
x -= 4 # x = x - 4
print(x)
print(f'el valor de x menos 4 es: {x}')

# multiplicar (*=)
x *= 2 # x = x * 2
print(x)
print(f'el valor de x multiplicado por 2 es {x}')