# 2. Classes and Objects

Class คือแม่แบบที่กำหนดข้อมูลและพฤติกรรม ส่วน object คือ instance ที่สร้างจาก class เดียวกัน แต่แต่ละ object สามารถเก็บข้อมูลของตนเองได้

```python
class Car:
    brand = "Toyota"

car1 = Car()
print(car1.brand)
```

การสร้าง object ใช้ชื่อ class ตามด้วยวงเล็บ เช่น `car1 = Car()`

**โค้ดทดลอง:** `examples/02_classes_objects.py`
