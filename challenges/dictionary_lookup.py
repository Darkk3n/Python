import os

os.system("cls" if os.name == "nt" else "clear")
# Dictionary Lookup: Ask for a fruit name and return the quantity from a stock dictionary. (e.g., "pears": 8).

fruits = {
    "pears": 8,
    "apples": 10,
    "pineapples": 5,
    "strawberries": 3,
    "berries": 7,
}
fruit = input("Provide a fruit name: ")

# if fruit not in fruits:
#     print("Fruit not found")
# else:
#     print(f"{fruit.capitalize()} amount is: {fruits[fruit]}")

print(fruits.get(fruit, "Fruit not found"))
