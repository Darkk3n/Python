from os import system

system("clear")

# The Membership Check: Check if an input username exists in ["admin", "root", "user123"]. Return a Boolean.

user_name: str = input("Enter user name: ")
print(user_name in ["admin", "root", "user123"])
