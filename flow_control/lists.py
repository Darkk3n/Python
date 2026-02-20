# Listas
# Secuencias mutables de elementos. Pueden contener elementos de cualquier tipo, incluso otras listas.
import os

os.system("clear")

print("\nListas:")
lista1 = [1, 2, 3, 4, 5]  # Lista de numeros
lista2 = ["Manzanas", "Peras", "Naranjas"]  # Lista de strings
lista3 = [
    1,
    "Hola",
    3.14,
    True,
]  # lista de tipos mixtos

lista_vacia = []
matrix = [[1, 2], [3, 4], [5, 6]]  # Lista que contiene otras listas

print("Lista 1:", lista1)
print("Lista 2:", lista2)
print("Lista 3:", lista3)
print("Lista vacia:", lista_vacia)
print("Lista de listas:", matrix)

# Acceso a elementos por indice
print("\nAcceso a elementos por indice:")

print(lista2[0])
print(lista3[2])
# Acceso a elementos por indice negativo (desde el final se empieza a contar desde -1)
print(lista2[-1])
print(lista2[-2])

print(matrix[1][0])

# Slicing (rebanado)

print("\nSlicing (rebanado):")

# Imprime los elementos desde el indice 1 hasta el indice 3 (el indice 4 no se incluye)
print(lista1[1:4])
# Imprime los elementos desde el inicio de la lista hasta el indice 2 (el indice 3 no se incluye)
print(lista1[:3])
# Imprime los elementos desde el indice 3 hasta el final de la lista
print(lista1[3:])
# Crear una copia de lista completa
print(lista1[:])

# Hay mas magia
lista1 = [1, 2, 3, 4, 5, 6, 7, 8]
# desde - hasta - paso (en relacion a los indices)
print(lista1[1::2])
# Invertir la lista
print(lista1[::-1])

# Modificar elementos de una lista
lista1[2] = 20
print(lista1)

# Agregar elementos a una lista
lista1 = [1, 2, 3]

# Concatenar listas
# Forma larga y menos eficiente
lista1 = lista1 + [4, 5, 6]
print(lista1)

# Forma corta y mas eficiente
lista1 += [7, 8]

# Recuperar longitud de una lista
print("\nLongitud de la lista:", len(lista1))
