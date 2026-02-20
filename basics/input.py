###
# Entrada de usuario - (input()) simplificado
# La funcion input() permite obtener datos del usuario a través de la consola.
###

print("¿Cuál es tu nombre?")
nombre = input()
print(f"El nombre es {nombre}")

age = input("Cual es tu edad?\n")
print(f"Dentro de 20 a;os tendras {int(age) + 20} a;os")

print("Obtener multiples valores a la vez")
country, city = input("Ingrese pais y ciudad vives?\n").split()
print(f"Vives en {city}, del pais {country}")
