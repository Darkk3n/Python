import os

os.system("cls" if os.name == "nt" else "clear")

# The List Cleaner: Use a loop (no set()) to remove duplicates from [1, 2, 2, 3, 4, 4, 4, 5]. (Result: [1, 2, 3, 4, 5]).

# nums: list[int] = [1, 2, 2, 3, 4, 4, 4, 5]

# for idx, num in enumerate(nums):
#     if idx >= len(nums):
#         break
#     elif nums[idx] == nums[idx + 1]:
#         nums.pop(idx)

# print(nums)

nums = [1, 2, 2, 3, 4, 4, 4, 5]
unique_nums = []

for n in nums:
    if n not in unique_nums:
        unique_nums.append(n)

print(unique_nums)
