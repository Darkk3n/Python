import os

os.system("cls" if os.name == "nt" else "clear")

# Even Stevens: Use range() to print all even numbers from 2 to 20.

print([even for even in range(2, 21) if even % 2 == 0])
