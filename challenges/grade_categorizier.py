import os

os.system("cls" if os.name == "nt" else "clear")

# Grade Categorizer: Loop through [88, 92, 45, 70, 65] and print "Pass" (70+) or "Fail".

grades: list[int] = [88, 92, 45, 70, 65]

# for grade in grades:
#     if grade >= 70:
#         print("Pass")
#     else:
#         print("Fail")

print(["Pass" if g >= 70 else "Fail" for g in grades])
