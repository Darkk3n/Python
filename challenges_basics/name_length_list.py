import os

os.system("cls" if os.name == "nt" else "clear")

# The Name Length List
# Given names = ["Alice", "Bob", "Cassandra", "Dave"], use list comprehension to create a list containing the length (number of characters) of each name.

names = ["Alice", "Bob", "Cassandra", "Dave"]

print([len(n) for n in names])
