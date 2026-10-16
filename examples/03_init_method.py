class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id

    def show_info(self):
        print(f"Name: {self.name}")
        print(f"Student ID: {self.student_id}")


if __name__ == "__main__":
    student = Student("Mali", "001")
    student.show_info()
