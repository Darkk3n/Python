import os

os.system("cls" if os.name == "nt" else "clear")

# Multi-Type Dictionary: Create a user dictionary with a name, age, and a list of hobbies. Print only the second hobby.

person = {
    "name": "Gerry",
    "age": 37,
    "hobbies": ["Video Games", "Ask Gemini for Python coding challenges"],
}

hobbie = person.get("hobbies", "Not found")
print(hobbie[1])
