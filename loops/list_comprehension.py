import os

os.system("clear")

animales = ["perro", "loro", "gato", "raton", "pez", "canario"]

animales_upper = [animal.upper() for animal in animales if len(animal) > 4]
# *Projection* for *Variable* in *List* *Optional Condition*

print(animales_upper)

# Muestra los numeros pares de una lista
# List comprehension con condicion
pares = [num for num in [1, 2, 3, 5, 6, 7, 8, 9, 10] if num % 2 == 0]

print(pares)
