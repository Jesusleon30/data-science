# frutas = ["banana", "manzana", "pera"]

# for fruta in frutas:
#     print(frutas)



# letras = "bienvenido"
# for letra in letras:
#     print(letra)





# # while
# contador = 1 
# while contador <= 5:
#     print (f'contador: {contador}')
#     contador += 1

# Ejercicio 1
# Validar la hora (hh) 24 hrs, en la cual:
# Si son mas de las 6 am, me muestre el mensaje vamos a trabajar
# Si son las 12 pm, me muestre es hora de almorzar
# Si son las 6 pm, me muestre es hora de salir del trabajo
# Si son las 10 pm, me muestre es hora de dormir

hora_actual = 23


if hora_actual >= 6 and hora_actual < 12 :
    print(f'vamos a trabajar que son las: {hora_actual}') 
elif hora_actual == 12:
    print(f'vamos a comer que son las: {hora_actual}')
elif hora_actual >=18 and hora_actual < 20:
    print(f'es ora de salir del trabajo que son las : {hora_actual}')
elif hora_actual >= 22:
    print(f'es ora de dormir que son las {hora_actual}')
else:
    print("no hay orarios")
