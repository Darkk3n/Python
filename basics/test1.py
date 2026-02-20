name: str = "Gerardo"
age: int = 37

print(f"My name is {name} and I am {age} years old.")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
processed = [n * 2 for n in numbers if n > 3]


print(processed)
