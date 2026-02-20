import os

os.system("cls" if os.name == "nt" else "clear")

# The "While" Countdown: Count down from 10 to 1 with a while loop, ending with "Blast off!".

counter = 10
while counter <= 10 and counter >= 1:
    print(counter)
    counter -= 1

print("Blass Off!")
