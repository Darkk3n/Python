import os

os.system("cls" if os.name == "nt" else "clear")

# The Dictionary Merger
# You have two dictionaries: stock_a = {"apples": 10, "orange": 5} and stock_b = {"apples": 5, "pears": 8}. Write logic to merge them into a total_stock dictionary. If a fruit exists in both, sum the values.

stock_a = {"apples": 10, "orange": 5}
stock_b = {"apples": 5, "pears": 8}

total_stock = stock_a.copy()

for fruit, amount in stock_b.items():
    if fruit in total_stock:
        total_stock[fruit] += amount
    else:
        total_stock[fruit] = amount

print(total_stock)
