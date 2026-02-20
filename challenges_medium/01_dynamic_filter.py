import os

os.system("cls" if os.name == "nt" else "clear")

# The Dynamic Filter (Refined "List Cleaner")
# Given a list of dictionaries representing products: [{"name": "Laptop", "price": 1200}, {"name": "Mouse", "price": 25}]. Write a function that takes a min_price and returns only the names of products that cost more than that, using a single line of list comprehension.

products = [
    {"name": "Laptop", "price": 1200},
    {"name": "Mouse", "price": 25},
    {"name": "Keyboard", "price": 50},
    {"name": "Charger", "price": 35},
]


def products_that_cost_more(min_price: int):
    # to_return = []
    # for product in products:
    #     if product["price"] > min_price:
    #         to_return.append(product["name"])
    # return to_return
    return [p["name"] for p in products if p["price"] > min_price]


print(products_that_cost_more(10))
print(products_that_cost_more(30))
print(products_that_cost_more(80))
print(products_that_cost_more(100))
