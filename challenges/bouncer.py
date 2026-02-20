from os import system

system("clear")

# The Bouncer: Check age. 21+ is "Access Granted", 18-20 is "Almost there", under 18 is "Access Denied".

age: int = int(input("Provide your age: "))
if age >= 21:
    print("Access Granted")
elif age >= 18 and age < 21:
    print("Almost there")
else:
    print("Access Denied")
