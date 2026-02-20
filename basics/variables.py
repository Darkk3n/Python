# Variables
# solo es necesario poner el nombre

my_name = "Gerardo"

print(my_name)


age = 32
print(age)

age = 37
print(age)

# Tipado fuerte: Python no realiza conversiones de forma automatica

# f-strings => string interpolation
# desde version 3.6
print(f"Hola {my_name}, tengo {age} años")

# No recomendada, forma de asignar variables
name, age2, city = "Gerardo", 32, "Madrid"

# convenciones de variables
# snake_case
mi_nombre_variable = "Gerardo"

print(mi_nombre_variable)

MiNombreVariable = "Gerardo"  # PascalCase
miNombreVariable = "Gerardo"  # camelCase
# NO RECOMENDADO

# No existen constantes en Python, pero se pueden usar mayusculas para indicar que no se deben modificar
MI_CONSTANTE = "No cambiar este valor"

# nombres no validos de variables
# 123_variable
# variable-123P
# variable 123

is_user_logged_in: bool = True  # Tipado dinamico y estatico
print(is_user_logged_in)

# is_user_logged_in = 42  # Aunque se puede asignar otro tipo de dato, no es recomendable, debido a la posibilidad del lenguaje de cambiar el tipo de dato
# print(is_user_logged_in)
