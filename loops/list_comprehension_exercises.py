import os

os.system("clear")

###
# EJERCICIOS (for)
###

# Ejercicio 1: Imprimir números pares
# Imprime todos los números pares del 2 al 20 (inclusive) usando un bucle for.
print("\nEjercicio 1:")
# for num in range(2, 20):
#     if num % 2 == 0:
#         print(num)


# Ejercicio 2: Calcular la media de una lista
# Dada la siguiente lista de números:
numeros = [10, 20, 30, 40, 50]
sum = 0
# Calcula la media de los números usando un bucle for.
print("\nEjercicio 2:")
# for num in numeros:
#     sum += num

# print(sum / len(numeros))

# Ejercicio 3: Buscar el máximo de una lista
# Dada la siguiente lista de números:
numeros = [15, 5, 25, 10, 20]
max = 0
# Encuentra el número máximo en la lista usando un bucle for.
print("\nEjercicio 3:")
# for idx, num in enumerate(numeros):
#     if id == 0:
#         max = num
#     elif numeros[idx] > numeros[idx + 1]:
#         max = numeros[idx + 1]

print(max)
# Ejercicio 4: Filtrar cadenas por longitud
# Dada la siguiente lista de palabras:
palabras = ["casa", "arbol", "sol", "elefante", "luna"]
# Crea una nueva lista que contenga solo las palabras con más de 5 letras
# usando un bucle for y list comprehension.
print("\nEjercicio 4:")

# print([palabra for palabra in palabras if len(palabra) > 5])

# Ejercicio 5: Contar palabras que empiezan con una letra
# Dada la siguiente lista de palabras:
palabras = ["casa", "arbol", "sol", "elefante", "luna", "coche"]
# Pide al usuario que introduzca una letra.
# Cuenta cuántas palabras en la lista empiezan con esa letra (sin diferenciar mayúsculas/minúsculas).
print("\nEjercicio 5:")

input_palabra = input("Escriba una palabra: ")
primera_letra = input_palabra[0]
contador = 0
for palabra in palabras:
    letra = palabra[0]
    if primera_letra == letra:
        contador += 1

print(
    f"\nPalabra escrita: {input_palabra}. Palabras del array con {primera_letra}: {contador}"
)
