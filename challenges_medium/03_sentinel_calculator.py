import os

os.system("cls" if os.name == "nt" else "clear")

# The "Sentinel" Calculator (Totalizer 2.0)
# Modify your Totalizer. It should keep asking for numbers, but if the user enters something that isn't a number (and isn't "stop"), it should print "Invalid input" and continue the loop without crashing or resetting the sum.

sum = 0
while True:
    command = input("Provide a number or stop: ")
    if command.upper() == "stop".upper():
        break
    elif not command.isdigit():
        print("Invalid input")
    else:
        sum += int(command)

print(sum)
