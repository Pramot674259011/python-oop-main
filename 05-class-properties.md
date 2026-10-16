# 5. Class Properties

Attribute ใช้เก็บข้อมูลของ class หรือ object โดย instance attribute มักกำหนดผ่าน `self` ส่วน class attribute ประกาศใน class และใช้ร่วมกันได้

```python
class Student:
    school = "NPRU"  # class attribute

    def __init__(self, name):
        self.name = name  # instance attribute
```

**โค้ดทดลอง:** `examples/05_class_properties.py`
