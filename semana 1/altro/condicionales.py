
# if -> ejecuta un bloque de codigo si la condicion es verdadera
# if edad >=18:
#     # ....
#     if edad ==65:
#         # ...
#         # al segundo if
#     # al primer if


# caso de uso 1

# Validar que el usuario sea mayor de edad (18 años).
edad = 16
print( edad >= 18) #condicion


# if -> ejecuta un bloque de codigo si la condicion es verdadera
# else -> ejecuta un bloque de codigo si la condicion anterior no es verdadera
# elif -> permite de agregar mas condiciones en caso el primero no se cumpla 


if edad >= 18:
    print("es mayor de edad!") 
else:
    print('es menor de edad!')

# operador ternario para cosas chicas 
print('Es mayor de edad') if edad >= 18 else print('Es menor de edad')

print("Python es practico!") #este siempre imprimira xk esta fuera del if 




# Caso de uso 2
# Validar el clima, para poder decidir si llevar un paragua o no
clima = "soleado"

if clima == "lloviendo":
    print("Llevar un paraguas")
elif clima == "nublado":
    print("Lleva un paraguas por si acaso")
else:
    print("No necesito paraguas")
