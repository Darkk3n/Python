import os

os.system("clear")

lista1 = ["a", "b", "c", "d"]

# Agrega un elemento al final de la lista
lista1.append("e")
print(lista1)

# Agrega un elemento en una posicion especifica
lista1.insert(1, "@")
print(lista1)

# Agrega varios elementos al final de la lista
lista1.extend(["f", "g", "h"])
print(lista1)

# Elimina un elemento por su valor
lista1.remove("@")
print(lista1)

# Elimina un elemento por su indice
lista1.pop(1)
print(lista1)

# Otra alternativa para eliminar un elemento por su indice
del lista1[1]

# Eliminar todos los elementos de la lista
lista1.clear()
print(lista1)

# Eliminar un rango de elementos
lista1 = ["🐨", "🐼", "🐵", "🐸"]
del lista1[1:3]
print(lista1)


# Ordenar Listas modificando original
numbers = [5, 2, 9, 1, 5, 6]
numbers.sort()
print(numbers)

# Ordenar Listas creando una nueva lista
numbers = [3, 10, 2, 8, 101, 99]
sorted_numbers = sorted(numbers)
print(sorted_numbers)
print(numbers)

# Ordenar listas de textos (todo minuscula)
frutas = ["manzana", "naranja", "banana", "kiwi", "manzana", "pera", "naranja"]
sorted_frutas = sorted(frutas)
print(sorted_frutas)

# Ordenar listas de textos (mezclas mayusculas y minusculas)
frutas = ["Manzana", "naranja", "banana", "Kiwi", "manzana", "pera", "naranja"]
frutas.sort(key=str.lower)
print(frutas)

# Mas metodos utiles
animals = ["🐨", "🐼", "🐵", "🐸", "🐼"]
# Devuelve la cantidad de elementos en la lista
print(len(animals))

# Contar
print(animals.count("🐼"))

# Comprobar si un elemento esta en la lista
print("🐼" in animals)
print("🐶" in animals)
