import os

os.system("clear")
# Ejercicio 1: Determinar el mayor de dos números
# Pide al usuario que introduzca dos números y muestra un mensaje
# indicando cuál es mayor o si son iguales

# print("Introduzca dos numeros:")
# num1 = int(input("Numero 1: "))
# num2 = int(input("Numero 2: "))

# if num1 > num2:
#     print(f"{num1} es mayor que {num2}")
# elif num2 > num1:
#     print(f"{num2} es mayor que {num1}")
# else:
#     print("Son iguales")

# Ejercicio 2: Calculadora simple
# Pide al usuario dos números y una operación (+, -, *, /)
# Realiza la operación y muestra el resultado (maneja la división entre zero)

# print("\nCalculadora:")
# operator = input("Ingrese una operacion (+, -, *, /): ")
# if operator not in "[+,-,*,/]":
#     print("Operacion invalida")
# else:
#     num1 = float(input("Numero 1: "))
#     num2 = float(input("Numero 2: "))
#     result = 0
#     if operator == "+":
#         result = num1 + num2
#     elif operator == "-":
#         result = num1 - num2
#     elif operator == "*":
#         result = num1 * num2
#     elif operator == "/":
#         if num2 == 0:
#             print("Error: No se puede dividir entre cero")
#         else:
#             result = num1 / num2
#     print(f"Resultado: {result}")

# Ejercicio 3: Año bisiesto
# Pide al usuario que introduzca un año y determina si es bisiesto.
# Un año es bisiesto si es divisible por 4, excepto si es divisible por 100 pero no por 400.
# year = int(input("\nIngrese un año: "))
# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#     print(f"{year} es un año bisiesto")
# else:
#     print(f"{year} no es un año bisiesto")

# Ejercicio 4: Categorizar edades
# Pide al usuario que introduzca una edad y la clasifique en:
# - Bebé (0-2 años)
# - Niño (3-12 años)
# - Adolescente (13-17 años)
# - Adulto (18-64 años)
# - Adulto mayor (65 años o más)

age = int(input("Ingrese una edad: "))
if age >= 0 and age <= 2:
    print("Bebe")
elif age >= 3 and age <= 12:
    print("Niño")
elif age >= 13 and age <= 17:
    print("Adolescente")
elif age >= 18 and age <= 64:
    print("Adulto")
elif age >= 65:
    print("Adulto mayor")
