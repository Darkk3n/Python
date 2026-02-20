from os import system

system("clear")

# Square Generator: Use list comprehension to get squares of numbers 1–10. (Result: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]).

result: list[int] = [squared**2 for squared in range(1, 11)]
print(result)
