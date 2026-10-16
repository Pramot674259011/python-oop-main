# 3. The `__init__()` Method

`__init__()` เป็น method พิเศษที่ Python เรียกเมื่อสร้าง object มักใช้กำหนดค่าเริ่มต้นให้ attribute

```python
class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id

student = Student("Mali", "001")
print(student.name)
```

**โค้ดทดลอง:** `examples/03_init_method.py`
