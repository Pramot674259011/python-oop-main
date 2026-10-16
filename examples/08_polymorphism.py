class Cat:
    def sound(self):
        return "Meow"


class Dog:
    def sound(self):
        return "Woof"


def make_sound(animal):
    print(animal.sound())


if __name__ == "__main__":
    make_sound(Cat())
    make_sound(Dog())
