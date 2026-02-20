import os

os.system("clear")

# For
# Permite ejecutar un bloque de codigo repetidamente mientras itera un iterable o una lista

# Iterar lista
fruits = ["manzana", "pera", "mandarina"]

# for fruit in fruits:  # Sintaxis demasiado similar a foreach de C#
#     print(fruit)

# Iterar otros tipos de datos iterables
cadena = "Gerardo"
# for caracter in cadena:
#  print(caracter)

# Recuperar el indice con for usando enumerate()
fruits = ["manzana", "pera", "mandarina"]
# for index, fruit in enumerate(fruits):
#     print(f"El indice de {fruit} es {index}")

# Bucles anidados
letras = ["a", "b", "c"]
numeros = [1, 2, 3]
# for letra in letras:
#     for num in numeros:
#         print(f"{letra.upper()}{num}")

animales = ["perro", "loro", "gato", "raton", "pez", "canario"]
for idx, animal in enumerate(animales):
    print(animal)
    if animal == "loro":
        print(f"El loro esta en el indice {idx}")
        break

animales = ["perro", "loro", "gato", "raton", "pez", "canario"]
for idx, animal in enumerate(animales):
    print(animal)
    if animal == "loro":
        continue
