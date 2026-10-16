# 9. Encapsulation

Encapsulation คือการรวมข้อมูลกับ method ที่จัดการข้อมูลไว้ใน class และออกแบบวิธีเข้าถึงข้อมูลอย่างเหมาะสม ใน Python ชื่อ attribute ที่ขึ้นต้นด้วย `__` จะใช้ name mangling เพื่อลดการเข้าถึงโดยตรง (ไม่ใช่ระบบ private ที่ปิดกั้นอย่างสมบูรณ์)

```python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def get_balance(self):
        return self.__balance
```

**โค้ดทดลอง:** `examples/09_encapsulation.py`
