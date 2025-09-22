# Django Test Project

โปรเจค Django สำหรับการทดสอบและพัฒนา พร้อมด้วย Views, URL routing, Regex URL patterns, Query Parameters และ Django Templates

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

- **หน้าหลัก**: `http://127.0.0.1:8000/` - แสดงหน้า HTML template พร้อม navigation
- **หน้าทดสอบ**: `http://127.0.0.1:8000/test/` - แสดงหน้าทดสอบ Django template features (variables, loops, dynamic data)
- **หน้าเกี่ยวกับ**: `http://127.0.0.1:8000/about/` - แสดงหน้า About template พร้อมข้อมูลโปรเจค
- **หน้าค้นหา**: `http://127.0.0.1:8000/search/{keyword}/{page}/` - เช่น `/search/python/1/`
- **หน้าวันที่**: `http://127.0.0.1:8000/date/{year}-{month}-{day}/` - เช่น `/date/2024-12-25/`
- **หน้าบทความรายปี**: `http://127.0.0.1:8000/articles/{year}/` - เช่น `/articles/2024/`
- **หน้าบทความรายเดือน**: `http://127.0.0.1:8000/articles/{year}/{month}/` - เช่น `/articles/2024/12/`
- **หน้าแผนที่**: `http://127.0.0.1:8000/map/` - รองรับ query parameters เช่น `?type=satellite&lat=13.7563&lon=100.5018&zoom=15&q=Bangkok`

## โครงสร้างโปรเจค

```
django_test/
├── .git/               # Git repository
├── manage.py           # ไฟล์สำหรับจัดการโปรเจค Django
├── db.sqlite3          # SQLite database
├── templates/          # Django templates directory
│   ├── index.html      # HTML template สำหรับหน้าหลัก
│   ├── test.html       # HTML template สำหรับทดสอบ Django features
│   └── about.html      # HTML template สำหรับหน้าเกี่ยวกับ
├── django_test/        # โฟลเดอร์หลักของโปรเจค
│   ├── __init__.py
│   ├── settings.py     # การตั้งค่าโปรเจค (มี TEMPLATES config)
│   ├── urls.py         # URL routing กับ path patterns และ regex
│   ├── views.py        # Views functions (ใช้ทั้ง HttpResponse และ render)
│   ├── wsgi.py         # WSGI configuration
│   ├── asgi.py         # ASGI configuration
│   └── __pycache__/    # Python cache files
└── README.md           # ไฟล์นี้
```

## Features ที่มีอยู่

### Views และ URL Patterns

โปรเจคนี้แสดงให้เห็นการใช้งาน URL patterns ทั้งแบบปกติ, แบบ Regex, Query Parameters, และ Django Templates:

1. **Index View** (`/`) - ใช้ Django Template
   - Function: `index(request)`
   - ใช้ `render()` แทน `HttpResponse`
   - ส่ง context data ไปยัง template
   - Template: `templates/index.html` พร้อม CSS styling
   - มี navigation links ไปยัง views อื่นๆ

2. **Test View** (`/test/`) - ใช้ Django Template พร้อม Dynamic Data
   - Function: `test(request)`
   - ใช้ `render()` พร้อม context variables
   - Template: `templates/test.html` พร้อม CSS styling
   - แสดง dynamic data: วันที่ปัจจุบัน, lists ของสีและดอกไม้
   - ใช้ Django template tags: `{% for %}` loops
   - แสดง template variables: `{{ title }}`, `{{ content }}`, `{{ date }}`
   - เหมาะสำหรับการเรียนรู้ Django template system และ context data
   - แสดง import handling: `from datetime import date as today_date`

3. **About View** (`/about/`) - ใช้ Django Template
   - Function: `about(request)`
   - ใช้ `render()` แสดงหน้าข้อมูลโปรเจค
   - Template: `templates/about.html` พร้อม CSS styling
   - แสดงข้อมูลเทคโนโลยีและฟีเจอร์ต่างๆ

4. **Search View** (`/search/<keyword>/<page>/`)
   - Function: `search(request, keyword, page)`
   - รับพารามิเตอร์ keyword และ page number
   - ตัวอย่าง: `/search/python/1/`

5. **Date View** (`/date/<year>-<month>-<day>/`)
   - Function: `date(request, year, month, day)`
   - แสดงวันที่ในรูปแบบที่กำหนด
   - ตัวอย่าง: `/date/2024-12-25/`
   - **หมายเหตุ**: function ชื่อ `date` ทำให้เกิด conflict กับ `from datetime import date`

6. **Year Archive View** (`/articles/<year>/`) - ใช้ Regex
   - Function: `year_archive(request, year)`
   - แสดงบทความประจำปี (4 หลัก)
   - ตัวอย่าง: `/articles/2024/`

7. **Month Archive View** (`/articles/<year>/<month>/`) - ใช้ Regex
   - Function: `month_archive(request, year, month)`
   - แสดงบทความประจำเดือน (2 หลัก)
   - ตัวอย่าง: `/articles/2024/12/`

8. **Maps View** (`/map/`) - ใช้ Query Parameters
   - Function: `maps(request)`
   - รับ query parameters: `type`, `lat`, `lon`, `zoom`, `q`
   - ตัวอย่าง: `/map/?type=satellite&lat=13.7563&lon=100.5018&zoom=15&q=Bangkok`
   - Default values: type=roadmap, lat=13.7245, lon=100.49.30, zoom=11

## Django Templates

### Template Configuration
- Templates directory: `templates/`
- กำหนดใน `settings.py` ใน `TEMPLATES['DIRS']`
- ใช้ `Path.joinpath(BASE_DIR, "templates")` เพื่อระบุ path

### Template Features ในโปรเจค
- `index.html` - หน้าหลักพร้อม HTML/CSS styling และ navigation menu
- `test.html` - หน้าทดสอบ Django template features:
  - Template variables: `{{ title }}`, `{{ content }}`, `{{ date }}`
  - Template tags: `{% for %}` loops สำหรับ lists
  - Dynamic data: วันที่ปัจจุบัน, arrays ของสีและดอกไม้
  - CSS styling พร้อม responsive design
- `about.html` - หน้าข้อมูลโปรเจคพร้อมรายละเอียดฟีเจอร์
- Context variables และ template inheritance concepts
- แสดงความแตกต่างของ template design ตั้งแต่แบบง่ายจนถึงซับซ้อน
- Responsive design พร้อม CSS styling (ในบาง templates)
- Demo links สำหรับทดสอบ URL patterns ต่างๆ

### Template Comparison
| Template | Style | Features | Purpose |
|----------|-------|----------|---------|
| `test.html` | CSS + Dynamic Data | Template variables, for loops, date display | Django template features demonstration |
| `index.html` | Full CSS + Navigation | Context vars, navigation menu, links | Complete homepage |
| `about.html` | Full CSS + Content | Static content, project info, features | Project information page |

## Common Issues และการแก้ไข

### 1. Name Conflict Issue
**ปัญหา**: `AttributeError: 'function' object has no attribute 'today'`
**สาเหตุ**: function `date()` ในไฟล์เดียวกันกับ `from datetime import date`
**วิธีแก้ไข**: ใช้ alias `from datetime import date as today_date`

### 2. render() Function Syntax
**ปัญหา**: `render()` รับ arguments ผิดรูปแบบ
**วิธีแก้ไข**: ใช้ `render(request, template_name, context)` (3 parameters เท่านั้น)

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
5. แก้ไข templates ใน `templates/` directory
6. เปรียบเทียบ template designs และ features ต่างๆ

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

### Template-based Views
```bash
# ทดสอบหน้าหลัก (จะเห็น HTML template พร้อม styling)
curl http://127.0.0.1:8000/

# ทดสอบหน้าทดสอบ (จะเห็น dynamic data และ template features)
curl http://127.0.0.1:8000/test/

# ทดสอบหน้าเกี่ยวกับ (จะเห็น detailed HTML)
curl http://127.0.0.1:8000/about/
```

### URL Patterns ปกติ
```bash
# ทดสอบการค้นหา (พารามิเตอร์ใน URL)
curl http://127.0.0.1:8000/search/django/1/

# ทดสอบหน้าวันที่
curl http://127.0.0.1:8000/date/2024-12-25/
```

### Regex URL Patterns
```bash
# ทดสอบบทความรายปี (ต้องเป็น 4 หลัก)
curl http://127.0.0.1:8000/articles/2024/

# ทดสอบบทความรายเดือน (ปี 4 หลัก, เดือน 2 หลัก)
curl http://127.0.0.1:8000/articles/2024/12/
```

### Query Parameters
```bash
# ทดสอบหน้าแผนที่ (ไม่มี parameters)
curl http://127.0.0.1:8000/map/

# ทดสอบหน้าแผนที่พร้อม query parameters
curl "http://127.0.0.1:8000/map/?type=satellite&lat=13.7563&lon=100.5018&zoom=15&q=Bangkok"

# ทดสอบด้วย partial parameters
curl "http://127.0.0.1:8000/map/?type=terrain&zoom=12"
```

## URL Patterns ที่ใช้ในโปรเจค

### แบบปกติ (path)
- ใช้สำหรับ URL patterns ธรรมดา
- รองรับ type converters เช่น `<str:keyword>`, `<int:page>`
- ตัวอย่าง: `path("test/", views.test, name="test")`

### แบบ Regex (re_path)
- ใช้ regular expressions สำหรับ pattern ที่ซับซ้อน
- `(?P<year>[0-9]{4})` - capture group ชื่อ year ที่ต้องเป็นตัวเลข 4 หลัก
- `(?P<month>[0-9]{2})` - capture group ชื่อ month ที่ต้องเป็นตัวเลข 2 หลัก

### แบบ Query Parameters (GET parameters)
- ใช้สำหรับ optional parameters ใน URL
- เข้าถึงผ่าน `request.GET.get('parameter_name', 'default_value')`
- ตัวอย่าง: `?type=satellite&lat=13.7563&lon=100.5018&zoom=15&q=Bangkok`
- เหมาะสำหรับการกรอง, การค้นหา, หรือการตั้งค่าต่างๆ

### Django Templates
- ใช้ `render()` function เพื่อส่ง context data ไปยัง template
- Template files อยู่ใน `templates/` directory
- สามารถใช้ template variables เช่น `{{ variable_name }}`
- รองรับ template tags เช่น `{% for %}`
- รองรับ HTML, CSS, และ JavaScript
- แสดงตัวอย่างตั้งแต่ basic จนถึง advanced features

## หมายเหตุ

- โปรเจคนี้ใช้สำหรับการทดสอบและเรียนรู้ Django
- Django version 5.2.6 กับ Python 3.10
- ฐานข้อมูล SQLite3 (db.sqlite3) ถูกสร้างแล้ว
- Admin interface ถูก comment ออกในไฟล์ urls.py
- แสดงการใช้งานใน 4 แนวทางหลัก:
  - Path patterns (ปกติ)
  - Regex patterns (ซับซ้อน)
  - Query parameters (GET parameters)
  - Django Templates (HTML rendering)
- แสดงความแตกต่างของ template designs:
  - `test.html` - แสดง Django template features (variables, loops, dynamic data)
  - `index.html` - แบบสมบูรณ์ พร้อม navigation และ styling
  - `about.html` - แบบ content-rich พร้อมข้อมูลครบถ้วน
- views.py ใช้ทั้ง `HttpResponse` และ `render()` เพื่อแสดงความแตกต่าง
- แสดงการแก้ไข common issues เช่น name conflicts และ syntax errors
- ตรวจสอบให้แน่ใจว่าได้เปิดใช้งาน conda environment ก่อนรันคำสั่งต่างๆ
- สำหรับ production ควรมีการตั้งค่าเพิ่มเติมด้านความปลอดภัยและประสิทธิภาพ
- SECRET_KEY ในไฟล์ settings.py เป็นแบบ development ไม่ควรใช้ใน production