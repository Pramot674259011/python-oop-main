# 4. The `self` Parameter

`self` ใช้อ้างถึง object ปัจจุบัน ทำให้ method เข้าถึง attribute และ method ของ object นั้นได้ โดยปกติจะเป็นพารามิเตอร์ตัวแรกของ instance method

```python
class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, {self.name}")
```

**โค้ดทดลอง:** `examples/04_self_parameter.py`
