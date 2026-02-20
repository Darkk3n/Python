import os

os.system("clear")

print("\nValores booleanos basicos:")
print(True)
print(False)

# Operadores de comparacion. Iguales a C#

print("\nOperadores de comparacion:")
print("5 > 3:", 5 > 3)  # True
print("5 < 3:", 5 < 3)  # False
print("5 == 5:", 5 == 5)  # True (Igualdad)
print("5 != 3:", 5 != 3)  # True (Desigualdad)
print("5 >= 5:", 5 >= 5)  # True (Mayor o igual)


print("\nCompracion de cadenas:")
# Lexicograficas
# La comparacion se realiza letra por letra, y se basa en el orden alfabetico
print("manzana < pera:", "manzana" < "pera")  # True
print(
    "'Hola' == 'hola':", "Hola" == "hola"
)  # False (Mayusculas y minusculas son diferentes)

# Operadores logicos
# AND, OR, NOT

# Ternaria
print("\nOperador ternario:")
age = 17
mensaje = "Mayor de edad" if age >= 18 else "Menor de edad"
print(f"Ternaria: {mensaje}")
