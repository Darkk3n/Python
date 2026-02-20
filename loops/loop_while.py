# Bucles: Permiten ejecutar un bloque de codigo bajo alguna condicion
import os

os.system("clear")
# While

# counter = 1
# while counter <= 5:
#     #  print(counter)
#     counter += 1

# While con break

# counter = 0
# while True:
#     #  print(counter)
#     counter += 1
#     if counter == 10:
#         break

# Bucle con continue

# counter = 0
# while counter < 10:
#     counter += 1
#     if counter % 2 == 0:
#         continue
#  print(counter)

# While con else

# counter = 0
# while counter < 5:
#     #  print(counter)
#     counter += 1
# else:
#  print("El bucle ha terminado")


# Pedir al usuario un numero que tiene ser positivo
num = -1
while num <= 0:
    try:
        numero = int(input("Escribe un numero positivo: "))
        if numero < 0:
            print("El numero debe ser positivo. Intenta de nuevo")
    except ValueError:
        print("No fue posible convertir a numero")

print(f"El numero que has introducido es: {num}")
