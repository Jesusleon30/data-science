
# que datos podrias solicitar a una persona

# class (clase) -> persona 
# propriedades de un objeto
# dni
# direccion
# correo
# nombre
# apellidos
# edad
# estado civil

# 1- objeto -> Juan
# 13234
# av a 123
# juan@tecsup.com
# juan
# alcantara
# 26
# soltero

# 2- objeto -> Alan
# 658769
# av a 6788
# alan@tecsup.com
# alan
# medina
# 28
# casado


##################################

# Imaginemos que estamos realizando un juego, donde tenemos a heroes y villanos.
# Cada personaje, tiene nombre, una vida, y puede realizar acciones como atacar o recibir daño.

# Definición de una clase
# Formato -> PascalCase
# PersonaVideojuego -> PascalCase
# personaVideojuego -> camelCase
# persona_videojuego -> snake_case




# CONSTRUCTOR:
# este tiene una class y dentro de el tiene una function y su parametro es self
#la function dentro una clase se le llama metodo

class Personaje:
    # self, hace referencia a todo lo que se encuentra en la clase
    # initialize
    def __init__(self, nombre, vida):
        self.nombre = nombre
        self.vida = vida  # atributo privado

    def atacar(self):
        return f'{self.nombre} esta atacando.'

    def recibir_danio(self, danio):
        self.vida -= danio
        return f'{self.nombre} recibio {danio} de daño. Vida restante: {self.vida}'

    # def obtener_vida(self):
    #     return self.__vida


# Clase Heroe herada de Personaje
class Heroe(Personaje):
    def curar(self):
        self.vida += 10
        return f'{self.nombre} se ha curado. Vida actual: {self.vida}'

    def atacar(self):
        return f'El Heroe {self.nombre} esta atacando.'


# Clase Villano hereda de Personaje
class Villano(Personaje):
    def usar_poder(self):
        return f'{self.nombre} esta usando su poder oscuro.'

    def atacar(self):
        return f'El Villano {self.nombre} esta atacando.'


# Crear nuestro objeto
heroe = Heroe('Cristian', 100)
print(f'El heroe {heroe.nombre}, tiene {heroe.vida} vida')
print(heroe.atacar())
print(heroe.curar())

villano = Villano('Carlos', 120)
print(f'El villano {villano.nombre}, tiene {villano.vida} vida')
print(villano.recibir_danio(30))
print(villano.usar_poder())
print(villano.atacar())
