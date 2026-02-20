# No 'public class User', just 'class'
class User:
    def __init__(self, name: str, age: int):
        self.name = name  # 'self' is like 'this'
        self.age = age

    def greet(self) -> str:
        # F-strings are your new best friend
        return f"Hello, my name is {self.name} and I am {self.age}."


# Entry point logic (Your 'static void Main')
if __name__ == "__main__":
    dev = User("Gemini", 10)
    print(dev.greet())
