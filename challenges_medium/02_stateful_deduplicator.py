import os

os.system("cls" if os.name == "nt" else "clear")

# The "Stateful" Deduplicator
# Write a script that takes a list with duplicates: [1, 5, 2, 1, 9, 1, 5, 10]. Create a new list that contains the unique values, but maintain the original order without using set().

duplicates = [1, 5, 2, 1, 9, 1, 5, 10]
unique_nums = []
for n in duplicates:
    if n not in unique_nums:
        unique_nums.append(n)

print(unique_nums)
