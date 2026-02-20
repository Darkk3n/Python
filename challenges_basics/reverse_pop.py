import os

os.system("cls" if os.name == "nt" else "clear")

# Reverse and Pop: Alphabetically sort ["Email", "Meeting", "Lunch", "Report"], pop the last item, and print the rest.

words = ["Email", "Meeting", "Lunch", "Report"]
words.sort()
words.pop()
print(words)
