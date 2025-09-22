# Django Test Project

โปรเจค Django สำหรับการทดสอบและพัฒนา

## ข้อกำหนดของระบบ

- Python 3.x
- Django
- Conda (สำหรับการจัดการ environment)

## การติดตั้งและการตั้งค่า

### 1. สร้างและเปิดใช้งาน Conda Environment

```bash
# สร้าง environment ใหม่ชื่อ django_test
conda create -n django_test python=3.x

# เปิดใช้งาน environment
conda activate django_test
```

### 2. ติดตั้ง Django

```bash
# ติดตั้ง Django ใน environment
pip install django
```

### 3. สร้างโปรเจค Django

```bash
# สร้างโปรเจค Django ในโฟลเดอร์ปัจจุบัน
django-admin startproject django_test .
```

## การรันโปรเจค

### เริ่มต้น Development Server

```bash
# รันเซิร์ฟเวอร์สำหรับพัฒนา
python manage.py runserver
```

หรือบน Windows:
```bash
python .\manage.py runserver
```

เซิร์ฟเวอร์จะรันที่ `http://127.0.0.1:8000/`

## โครงสร้างโปรเจค

```
django_test/
├── manage.py           # ไฟล์สำหรับจัดการโปรเจค Django
├── django_test/        # โฟลเดอร์หลักของโปรเจค
│   ├── __init__.py
│   ├── settings.py     # การตั้งค่าโปรเจค
│   ├── urls.py         # URL routing
│   ├── wsgi.py         # WSGI configuration
│   └── asgi.py         # ASGI configuration
└── README.md           # ไฟล์นี้
```

## คำสั่งที่มีประโยชน์

```bash
# เช็คโครงสร้างโปรเจค
dir                     # Windows
ls                      # macOS/Linux

# สร้าง app ใหม่
python manage.py startapp [app_name]

# ทำ migration
python manage.py makemigrations
python manage.py migrate

# สร้าง superuser
python manage.py createsuperuser

# เก็บข้อมูล static files
python manage.py collectstatic
```

## การพัฒนา

1. เปิดใช้งาน conda environment ก่อนเสมอ: `conda activate django_test`
2. รันเซิร์ฟเวอร์: `python manage.py runserver`
3. เข้าถึงเว็บไซต์ที่ `http://127.0.0.1:8000/`

## หมายเหตุ

- โปรเจคนี้ใช้สำหรับการทดสอบและเรียนรู้ Django
- ตรวจสอบให้แน่ใจว่าได้เปิดใช้งาน conda environment ก่อนรันคำสั่งต่างๆ
- สำหรับ production ควรมีการตั้งค่าเพิ่มเติมด้านความปลอดภัยและประสิทธิภาพ