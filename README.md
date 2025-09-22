# Django Test Project

โปรเจค Django สำหรับการทดสอบและพัฒนา พร้อมด้วย Views และ URL routing เบื้องต้น

## ข้อกำหนดของระบบ

- Python 3.10
- Django 5.2.6
- Conda (สำหรับการจัดการ environment)
- Git (สำหรับ version control)

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

### หน้าเว็บที่สามารถเข้าถึงได้

- **หน้าหลัก**: `http://127.0.0.1:8000/` - แสดง "Hello, world. You're at the index."
- **หน้าเกี่ยวกับ**: `http://127.0.0.1:8000/about/` - แสดง "This is the about page."
- **หน้าค้นหา**: `http://127.0.0.1:8000/search/{keyword}/{page}/` - เช่น `/search/python/1/`
- **หน้าวันที่**: `http://127.0.0.1:8000/date/{year}-{month}-{day}/` - เช่น `/date/2024-12-25/`

## โครงสร้างโปรเจค

```
django_test/
├── .git/               # Git repository
├── manage.py           # ไฟล์สำหรับจัดการโปรเจค Django
├── db.sqlite3          # SQLite database
├── django_test/        # โฟลเดอร์หลักของโปรเจค
│   ├── __init__.py
│   ├── settings.py     # การตั้งค่าโปรเจค
│   ├── urls.py         # URL routing กับ path patterns
│   ├── views.py        # Views functions (เพิ่มใหม่)
│   ├── wsgi.py         # WSGI configuration
│   ├── asgi.py         # ASGI configuration
│   └── __pycache__/    # Python cache files
└── README.md           # ไฟล์นี้
```

## Features ที่มีอยู่

### Views และ URL Patterns

1. **Index View** (`/`)
   - Function: `index(request)`
   - แสดงข้อความต้อนรับ

2. **About View** (`/about/`)
   - Function: `about(request)`
   - แสดงข้อมูลเกี่ยวกับหน้าเว็บ

3. **Search View** (`/search/<keyword>/<page>/`)
   - Function: `search(request, keyword, page)`
   - รับพารามิเตอร์ keyword และ page number
   - ตัวอย่าง: `/search/python/1/`

4. **Date View** (`/date/<year>-<month>-<day>/`)
   - Function: `date(request, year, month, day)`
   - แสดงวันที่ในรูปแบบที่กำหนด
   - ตัวอย่าง: `/date/2024-12-25/`

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
4. ทดสอบ URL patterns ต่างๆ ตามที่ระบุในส่วน Features

## การจัดการ Git

โปรเจคนี้มี Git repository แล้ว สามารถใช้คำสั่งต่อไปนี้:

```bash
# เช็คสถานะ
git status

# เพิ่มไฟล์
git add .

# Commit การเปลี่ยนแปลง
git commit -m "Your commit message"

# Push ไปยัง remote repository (ถ้ามี)
git push origin master
```

## การทดสอบ Views

สามารถทดสอบ views ต่างๆ ได้ดังนี้:

```bash
# ทดสอบหน้าหลัก
curl http://127.0.0.1:8000/

# ทดสอบหน้าเกี่ยวกับ
curl http://127.0.0.1:8000/about/

# ทดสอบการค้นหา
curl http://127.0.0.1:8000/search/django/1/

# ทดสอบหน้าวันที่
curl http://127.0.0.1:8000/date/2024-12-25/
```

## หมายเหตุ

- โปรเจคนี้ใช้สำหรับการทดสอบและเรียนรู้ Django
- Django version 5.2.6 กับ Python 3.10
- ฐานข้อมูล SQLite3 (db.sqlite3) ถูกสร้างแล้ว
- Admin interface ถูก comment ออกในไฟล์ urls.py
- ตรวจสอบให้แน่ใจว่าได้เปิดใช้งาน conda environment ก่อนรันคำสั่งต่างๆ
- สำหรับ production ควรมีการตั้งค่าเพิ่มเติมด้านความปลอดภัยและประสิทธิภาพ
- SECRET_KEY ในไฟล์ settings.py เป็นแบบ development ไม่ควรใช้ใน production