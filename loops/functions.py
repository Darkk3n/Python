import os

os.system("clear")

""" Definicion de una funcion
def nombre_de_la_funcion(param1, param2, ...)
   # docstring
   # comentarios
   # codigo de la funcion
   return valor_de_retorno #opcional
"""

# Ejemplo de funcion


def saludar():
    print("Hola")


saludar()


# Ejemplo de funcion con parametro
def saludar_a(nombre):
    print(f"Hola {nombre}")


saludar_a("Gerardo")


# Funcion con mas parametros
def sumar(num1: int, num2: int):
    return num1 + num2


# resultado = sumar(5,10)
# print(resultado)
print(sumar(5, 10))

# Documentar funciones con docstring


def restar(a: int, b: int):
    """Resta dos numeros y devuelve el resultado"""

    return a - b


# Parametros por defecto
def multiplicar(a: int, b: int = 2):
    return a * b


print(multiplicar(5))


def describir_persona(nombre, edad, sexo):
    print(f"Soy {nombre} tengo {edad} a;os y me identifico como {sexo}")


# Los parametros son posicionales
describir_persona("Gerardo", 37, "Hombre")
describir_persona(37, "Hombre", "Gerardo")


# Parametros nombrados
describir_persona(sexo="Hombre", nombre="Gerardo", edad=37)


# Argumentos de longitud de variable(*args):


def sumar_numeros(*args):
    sum = 0
    for num in args:
        sum += num
    return sum


print(sumar_numeros(1, 2, 3, 45, 6, 7, 8, 8))
print(sumar_numeros(1, 2, 6, 7, 8, 8))

# Argumentos de clave-valor variable (**kwargs):


def mostrar_informacion_de(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


mostrar_informacion_de(sexo="Hombre", nombre="Gerardo", edad=37)
print("\n")
mostrar_informacion_de(nombre="Yessica", edad=35, sexo="Mujer")
print("\n")
mostrar_informacion_de(sexo="Test", nombre="Foo", edad=100)
