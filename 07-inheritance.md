# 7. Inheritance

Inheritance คือการสร้าง class ลูกให้สืบทอด attribute และ method จาก class แม่ ช่วยนำโค้ดเดิมกลับมาใช้ซ้ำ `super()` ใช้เรียกการทำงานจาก class แม่

```python
class Animal:
    def speak(self):
        print("Animal sound")

class Dog(Animal):
    def speak(self):
        print("Woof!")
```

**โค้ดทดลอง:** `examples/07_inheritance.py`
