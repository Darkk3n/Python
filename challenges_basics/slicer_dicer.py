from os import system

system("clear")
# The Slicer & Dicer: From colors = ["red", "blue", "green", "yellow", "orange", "purple"], slice the middle two colors. (Result: ['green', 'yellow']).

colors: list[str] = ["red", "blue", "green", "yellow", "orange", "purple"]
print(colors[2:4])
