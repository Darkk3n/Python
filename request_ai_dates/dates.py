from datetime import datetime, timedelta
from os import system

system("clear")

# Fecha y hora actual
print(datetime.now())

# Fecha y hora especifica
specific_date = datetime(2026, 2, 17)

print(specific_date)

# Formatear fechas
# metodo strftime()
now = datetime.now()
formatted_date = now.strftime("%d/%m/%Y")
print(formatted_date)

# Operaciones con fechas
yesterday = datetime.now() - timedelta(days=1)
print(yesterday)

tomorrow = datetime.now() + timedelta(days=1)
print(tomorrow)

one_hour_after = datetime.now() + timedelta(hours=1)
print(one_hour_after)

# Obtener componentes individuales de una fecha

year = now.year
print(year)
