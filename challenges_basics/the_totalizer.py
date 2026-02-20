import os

os.system("cls" if os.name == "nt" else "clear")

sum = 0
while True:
    command = input("Provide a number or stop: ")
    if command.upper() == "stop".upper():
        break
    else:
        sum += int(command)

print(sum)
