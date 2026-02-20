from os import system

system("clear")

persona = {
    "nombre": "Gerardo",
    "edad": 25,
    "calificaciones": [10, 9, 8, 9, 10],
    "socials": {"x": "Darkk3n", "facebook": "Darkk3n"},
}

# Acceder a valores
print(persona["socials"]["x"])
print(persona["nombre"])

# Actualizar valores
persona["nombre"] = "Aguilar"
print(persona["nombre"])

# Eliminar propiedades
del persona["calificaciones"]

print(persona)

# Obtener individualmente un valor y eliminar la llave del mismo
edad = persona.pop("edad")
print(f"Edad: {edad}")
print(persona)

# Sobreescribir un diccionario con otro

a = {"name": "Gerardo", "age": 37}
b = {"name": "Aguilar", "age": 25}

print(a)
a.update(b)
print(a)

# Comprobar si existe una propiedad

print("name" in persona)
print("nombre" in persona)

# Obtener todos los valores
print(persona.keys())
print(persona.values())
print(persona.items())
