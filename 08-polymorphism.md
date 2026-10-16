# 8. Polymorphism

Polymorphism หมายถึงการมีหลายรูปแบบ เช่น object ต่าง class มี method ชื่อเดียวกัน แต่ให้ผลลัพธ์ต่างกัน ผู้เรียกสามารถใช้ method ชื่อเดียวกันกับ object หลายชนิดได้

```python
class Cat:
    def sound(self):
        return "Meow"

class Dog:
    def sound(self):
        return "Woof"

for animal in (Cat(), Dog()):
    print(animal.sound())
```

**โค้ดทดลอง:** `examples/08_polymorphism.py`
