import os

os.system("cls" if os.name == "nt" else "clear")

# The "Chunker"
# Write a function that takes a list and a size n. It should return a list of lists, where each sub-list has n elements.
# Input: [1, 2, 3, 4, 5, 6], size=2 → Output: [[1, 2], [3, 4], [5, 6]].


def the_chunker(lst: list[int], size: int):
    #  to_return = []
    #  for i in range(0, len(lst), size):
    #      chunk = lst[i : i + size]
    #      to_return.append(chunk)
    #  return to_return
    return [lst[i : i + size] for i in range(0, len(lst), size)]


print(the_chunker([1, 2, 3, 4, 5, 6], 2))
