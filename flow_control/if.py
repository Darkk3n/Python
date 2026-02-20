import os

os.system("clear")

print("Sentencia simple condicional ")
edad = 18
if edad >= 18:
    print("Eres mayor de edad")

edad = 17
print("\nSentencia condicional con else")
if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")

print("\nSentencia condicional con elif")
nota = 5
if nota >= 9:
    print("Sobresaliente")
elif nota >= 7:
    print("Notable")
elif nota >= 6:
    print("Aprobado a lo minimo")
else:
    print("Reprobado")

print("\nCondiciones multiples")

# Javascript y otros
# && -> and
# || -> or

edad = 28
tiene_carnet = False

if edad >= 18 and tiene_carnet:
    print("Puede conducir")
else:
    print("No puede conducir")

if edad >= 18 or tiene_carnet:
    print("Puede conducir 🚗")
else:
    print("Paga al policia y te deja conducir 🚓")

# ! -> not

es_fin_de_semana = False
if not es_fin_de_semana:
    print("Tengo que trabajar")
else:
    print("Es fin de semana, puedo descansar")

print("\nAnidar condicionales")
edad = 20
tiene_dinero = True
if edad >= 18:
    if tiene_dinero:
        print("Puedes divertirte")
    else:
        print("Queda en casa")
else:
    print("Eres menos e dad, no puedes salir")
