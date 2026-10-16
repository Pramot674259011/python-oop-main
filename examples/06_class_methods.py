class Student:
    school = "Nakhon Pathom Rajabhat University"

    @classmethod
    def show_school(cls):
        print("School:", cls.school)


if __name__ == "__main__":
    Student.show_school()
