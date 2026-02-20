from os import system

system("clear")
# The Tip Calculator: Ask for a bill amount and number of people. Calculate a 15% tip and show what each person owes. (Result: 17.25 for a $60 bill / 4 people).

amount: float = float(input("Provide the bill amount: "))
amount_plus_tip: float = round(amount + (amount * 0.15))
amount_divided: float = amount_plus_tip / 4

print(f"Amount Plust Tip: {amount_plus_tip}")
print(f"Amount divided by 4 people: {amount_divided}")
