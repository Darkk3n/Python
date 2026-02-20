import os
from datetime import datetime

os.system("cls" if os.name == "nt" else "clear")

# Date Difference: Calculate the number of days between today and January 1st, 2026.

now = datetime.now()

# print(now - datetime(2026, 1, 1))
print((now - (datetime(2026, 1, 1))).days)
