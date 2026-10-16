class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, {self.name}!")


if __name__ == "__main__":
    person1 = Person("Mali")
    person2 = Person("Somchai")
    person1.greet()
    person2.greet()
