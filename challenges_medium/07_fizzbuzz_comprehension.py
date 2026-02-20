import os

os.system("cls" if os.name == "nt" else "clear")

# The FizzBuzz Comprehension
# The classic FizzBuzz (1 to 50), but it must be solved entirely inside a single List Comprehension.

result = [
    "FizzBuzz" if n % 15 == 0 else "Buzz" if n % 5 == 0 else "Fizz" if n % 3 == 0 else n
    for n in range(1, 51)
]

for r in result:
    print(r)
