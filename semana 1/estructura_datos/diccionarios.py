

#  Diccionarios - clave(string) -> valor(qualquier tipo de dato)

# este no tiene un indice
# una vez que tu accededes al valor puedes hacer acceder como deceas

diccionario = {
    # "clave": "valor",
    "nombre": "Renato",
    'apellidos': 'Condori Canza',
    'especialidades': [
        {
            'nombre': 'backend',
            'nivel': 'Sr'
        },
        {
            'nombre': 'Fronted',
            'nivel': 'Mid'
        }
    ]
}

# el modo correcto de escrivir para concatenar respetando las comillas depende del cierre de comillas

# primo modo:
print(f'Nombre: {diccionario["nombre"]}')

# segundo modo:
print(f"Nombre: {diccionario['nombre']}")

# ojo cada vez que quiero acceder al diccionario tengo que meter todo el codigo

print(f"Especialidades: {diccionario['especialidades']}")

# una vez que hemos accedido al valor hy recien podemos acceder al indice
print(f"Especialidades: {diccionario['especialidades'][0]}")
print(f"Especialidades: {diccionario['especialidades'][1]}")

# otro tipo creando una variable para reducir xk sonn cosas que se repiten
especialidades = diccionario['especialidades']
print(f"Especialidades: {especialidades}")
print(f"1-Especialidades: {especialidades[0]}")
print(f"2-Especialidades: {especialidades[1]}")


print(f"1-Especialidades: {especialidades[0]['nombre']}")
print(f"2-Especialidades: {especialidades[1]['nivel']}")