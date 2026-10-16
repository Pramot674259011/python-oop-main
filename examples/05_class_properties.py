class Student:
    school = "Nakhon Pathom Rajabhat University"

    def __init__(self, name):
        self.name = name


if __name__ == "__main__":
    student1 = Student("Mali")
    student2 = Student("Somchai")
    print(student1.name, "studies at", student1.school)
    print(student2.name, "studies at", student2.school)
