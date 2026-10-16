# 6. Class Methods

Instance method ทำงานกับ object ผ่าน `self` ส่วน class method ใช้ `@classmethod` และรับ `cls` เพื่อเข้าถึงข้อมูลระดับ class

```python
class Student:
    school = "NPRU"

    @classmethod
    def show_school(cls):
        print(cls.school)
```

**โค้ดทดลอง:** `examples/06_class_methods.py`
