# 1. Python OOP

OOP ย่อมาจาก Object-Oriented Programming เป็นแนวคิดการเขียนโปรแกรมโดยจัดข้อมูลและพฤติกรรมที่เกี่ยวข้องให้อยู่ใน object ทำให้โค้ดเป็นระเบียบ นำกลับมาใช้ซ้ำ และดูแลรักษาได้ง่ายขึ้น

## ตัวอย่าง
```python
class Student:
    def introduce(self):
        print("Hello, I am a student.")

student = Student()
student.introduce()
```

`Student` คือ class และ `student` คือ object ที่สร้างจาก class นั้น

## ข้อดี
- จัดโครงสร้างโปรแกรมเป็นส่วน ๆ
- ลดการเขียนโค้ดซ้ำ
- แก้ไขและทดสอบได้ง่ายขึ้น

**โค้ดทดลอง:** `examples/01_python_oop.py`
