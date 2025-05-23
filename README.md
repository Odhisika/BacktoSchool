# 🎒 BacktoSchool

BacktoSchool is a modern Django-based e-commerce platform tailored to meet all the needs of students when school resumes—or while they're in school. It's a **one-stop-shop** for parents, guardians, and students to conveniently buy school essentials in one place.

## 🛍️ Project Overview

**BacktoSchool** aims to make back-to-school shopping stress-free and streamlined. Whether it's textbooks, uniforms, stationery, tech gadgets, or lunch boxes — we’ve got it all covered.

### 👨‍👩‍👧‍👦 For Parents & Guardians

- Easily find everything your child needs for school
- Buy multiple items from different categories in a single checkout
- Get doorstep delivery or pick-up options

### 📚 For Students

- Find the latest books and learning tools
- Shop by class level or educational stage

---

## 🚀 Features

- 🔐 User authentication and registration
- 🛒 Fully functional shopping cart
- 💳 Checkout with payment gateway integration (Coming soon)
- 📦 Order tracking and management
- 📚 Categorized products (Books, Stationery, Uniforms, Electronics, etc.)
- 🧾 Invoice generation
- 📬 Email notifications for orders and confirmations
- 🛠️ Admin dashboard for product and order management

---

## 🛠 Tech Stack

- **Backend**: Django, Django REST Framework
- **Frontend**: HTML, CSS, Bootstrap (Optional: React for a SPA experience)
- **Database**: SQLite
- **Authentication**: Django Allauth / Custom

---

## 📦 Installation Guide

1. **Clone the repository**

   ```bash
   git clone https://github.com/Odhisika/BacktoSchool.git
   cd backtoschool
   ```

2. create a virtual environment
   python -m venv env
   source env/bin/activate # On Windows use `env\Scripts\activate`

3.Install dependencies

-pip install -r requirements.txt

4. Configure the environment variables

Rename .env.example to .env

Add your secret key, DB credentials, etc.

-Apply migrations

5. python manage.py migrate

6. Create superuser
   -python manage.py createsuperuser

7. Run the server
   -python manage.py runserver
