# Python OOP

Repository นี้รวบรวมสรุปภาษาไทยและไฟล์ตัวอย่างที่ทดลองรันได้ สำหรับเรียนรู้แนวคิดการเขียนโปรแกรมเชิงวัตถุ (Object-Oriented Programming: OOP) ในภาษา Python โดยเรียบเรียงเนื้อหาตามหัวข้อจาก [W3Schools — Python OOP](https://www.w3schools.com/python/python_oop.asp)

> ตัวอย่างโค้ดแบ่งเป็นไฟล์ย่อยตามหัวข้อ เพื่อให้อ่าน ทดลองแก้ไข และรันแต่ละแนวคิดได้สะดวก

## ผู้จัดทำ

- **ชื่อ:** นายวรรษพจน์ ศรีพลอยรุ่ง
- **รหัสนักศึกษา:** 674259012
- **สาขาวิชา:** วิศวกรรมซอฟต์แวร์

## เนื้อหาใน repository

| ลำดับ | หัวข้อ | เอกสารสรุป | ไฟล์ตัวอย่าง |
|---:|---|---|---|
| 1 | ภาพรวม Python OOP | [01-python-oop.md](01-python-oop.md) | [01_python_oop.py](examples/01_python_oop.py) |
| 2 | Classes and Objects | [02-classes-objects.md](02-classes-objects.md) | [02_classes_objects.py](examples/02_classes_objects.py) |
| 3 | The `__init__()` Method | [03-init-method.md](03-init-method.md) | [03_init_method.py](examples/03_init_method.py) |
| 4 | The `self` Parameter | [04-self-parameter.md](04-self-parameter.md) | [04_self_parameter.py](examples/04_self_parameter.py) |
| 5 | Class Properties | [05-class-properties.md](05-class-properties.md) | [05_class_properties.py](examples/05_class_properties.py) |
| 6 | Class Methods | [06-class-methods.md](06-class-methods.md) | [06_class_methods.py](examples/06_class_methods.py) |
| 7 | Inheritance | [07-inheritance.md](07-inheritance.md) | [07_inheritance.py](examples/07_inheritance.py) |
| 8 | Polymorphism | [08-polymorphism.md](08-polymorphism.md) | [08_polymorphism.py](examples/08_polymorphism.py) |
| 9 | Encapsulation | [09-encapsulation.md](09-encapsulation.md) | [09_encapsulation.py](examples/09_encapsulation.py) |
| 10 | Inner Classes | [10-inner-classes.md](10-inner-classes.md) | [10_inner_classes.py](examples/10_inner_classes.py) |

## แนวคิดสำคัญ

- **Class** คือแม่แบบที่กำหนดข้อมูลและพฤติกรรม
- **Object** คือสิ่งที่สร้างขึ้นจาก class
- **Attribute** ใช้เก็บข้อมูลของ class หรือ object
- **Method** คือฟังก์ชันที่ประกาศภายใน class
- **Inheritance** ช่วยให้ class ลูกนำคุณสมบัติและการทำงานจาก class แม่มาใช้ต่อได้
- **Polymorphism** ทำให้ object ต่างชนิดตอบสนองต่อ method เดียวกันได้หลายรูปแบบ
- **Encapsulation** รวมข้อมูลและการทำงานไว้ใน class พร้อมกำหนดวิธีเข้าถึงข้อมูล
- **Inner class** คือ class ที่ประกาศภายใน class อื่น

## เริ่มต้นใช้งานผ่าน VS Code

1. ติดตั้ง [Python 3](https://www.python.org/downloads/) และ [Visual Studio Code](https://code.visualstudio.com/) หากยังไม่มี
2. เปิด VS Code แล้วเลือก **File → Open Folder...** จากนั้นเลือกโฟลเดอร์ repository นี้
3. เปิดไฟล์ `.md` เพื่ออ่านสรุป หรือเปิดไฟล์ในโฟลเดอร์ `examples/` เพื่อดูและแก้ไขโค้ด
4. เปิด Terminal ใน VS Code ด้วย **Terminal → New Terminal**
5. รันตัวอย่างโดยใช้คำสั่ง:

```bash
python examples/01_python_oop.py
```

เปลี่ยนชื่อไฟล์เพื่อทดลองหัวข้ออื่น เช่น:

```bash
python examples/07_inheritance.py
python examples/09_encapsulation.py
```

ตัวอย่างใช้ไลบรารีมาตรฐานของ Python จึงไม่ต้องติดตั้งแพ็กเกจเพิ่มเติม หากคำสั่ง `python` ใช้ไม่ได้ ให้ลองใช้ `py` บน Windows:

```powershell
py examples/01_python_oop.py
```

## โครงสร้างไฟล์

```text
python-oop-main/
├── README.md
├── 01-python-oop.md
├── 02-classes-objects.md
├── ...
├── 10-inner-classes.md
└── examples/
    ├── 01_python_oop.py
    ├── 02_classes_objects.py
    ├── ...
    └── 10_inner_classes.py
```

ไฟล์ Markdown แต่ละไฟล์มีสรุปแนวคิดและลิงก์ไปยังโค้ดตัวอย่างที่เกี่ยวข้อง สามารถแก้ไขและทดลองโค้ดใน VS Code ได้โดยตรง

## แหล่งอ้างอิง

- [W3Schools — Python OOP](https://www.w3schools.com/python/python_oop.asp)
- [W3Schools — Python Classes](https://www.w3schools.com/python/python_classes.asp)
- [W3Schools — Python Inheritance](https://www.w3schools.com/python/python_inheritance.asp)
- [W3Schools — Python Polymorphism](https://www.w3schools.com/python/python_polymorphism.asp)
- [W3Schools — Python Encapsulation](https://www.w3schools.com/python/python_encapsulation.asp)
