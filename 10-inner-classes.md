# 10. Inner Classes

Inner class คือ class ที่ประกาศอยู่ภายใน class อื่น เหมาะกับกรณีที่ class ด้านในเกี่ยวข้องกับ class ด้านนอกโดยเฉพาะ

```python
class Computer:
    class CPU:
        def info(self):
            print("CPU component")

cpu = Computer.CPU()
cpu.info()
```

**โค้ดทดลอง:** `examples/10_inner_classes.py`
