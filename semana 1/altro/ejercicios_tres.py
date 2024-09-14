
'''
# ejercicico 1

1. crear una clase calculadora.
2. la calculadora debe tener metodos para realizar las operaciones suma, resta, multiplicacion y division.
3. El usuario debera ingresar 2 numeros (float), luego  seleccionar la operacion que desea realizzaar.
4. mostrar el resultado final: la {operacion} de los numeros: {n1}, {n2} da como resultado: {resultado}

'''

'''

class Calculadora():
    def __init__(self, numero_uno, numero_dos):
        self.numero_uno = numero_uno
        self.numero_dos = numero_dos


    def sumar(self):
        return self.numero_uno + self.numero_dos
    
    def restar(self):
        return self.numero_uno - self.numero_dos
    
    def multiplicar(self):
        return self.numero_uno * self.numero_dos
    
    def dividir(self):
        if self.numero_dos != 0:
             return self.numero_uno / self.numero_dos
        else:
            return "no se puede dividir por 0"
        

numero_uno = float(input("ingrese el primer numero: "))
numero_dos = float(input("ingrese el segundo numero: "))
operacion = input("ingrese la operacion (sumar, restar, multiplicar, dividir): ")

calculadora = Calculadora(numero_uno, numero_dos)

if operacion == 'sumar':
    resultado = calculadora.sumar()
elif operacion == 'restar':
    resultado = calculadora.restar()
elif operacion == 'multiplicar':
    resultado = calculadora.multiplicar()
elif operacion == 'dividir':
    resultado = calculadora.dividir()
else:
    resultado = 'Operación no valida'


print(
    f'El resultado de {operacion} {numero_uno} y {numero_dos} es: {resultado}'
)

'''

    
# Ejercicio 2
'''
1. Crear una clase Tareas que administre una lista de tareas pendientes.
2. El usuario podrá agregar, eliminar y ver tareas.
3. Utilizar input para permitir que el usuario realice las acciones.
4. Utilizar while, para que el programa se siga ejecutando hasta que el usuario decida salir.
5. Mostrar las tareas con un salto de linea, usando f-string.
'''

while True:
    print('''
    1. Agregar tarea
    2. Eliminar tarea
    3. Ver tareas
    4. Salir
    ''')

    opcion = input('Seleccione una opcion: ')

    if opcion == '1':
        print('Agregamos una tarea')
    elif opcion == '2':
        print('Eliminamos una tarea')
    elif opcion == '3':
        print('Mostrar todas las tareas')
    elif opcion == '4':
        print('Saliendo del programa')
        break # sale del bucle while
    else:
        print('Opcion no valida, intente nuevamente')



utiles_escuela = ["lapiz", "cuaderno", "borrador", "libro"]
print(f'inicio -> {utiles_escuela}')

utiles_escuela.append("lapicero")
print(f'append -> {utiles_escuela}')

