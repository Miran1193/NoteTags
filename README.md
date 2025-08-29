# 📝 NoteApp — Notes with Tags

## 📌 Description
**NoteApp** is a Django-based web application for creating, editing, and managing notes.  
Each note can be assigned one or more tags for easy filtering and organization.  
The app supports user registration, authentication, and personal access to notes.

---

## 🚀 Features
- User registration and login 🔐  
- Create, edit, and delete notes ✏️  
- Tag support (#work, #personal, etc.) 🏷️  
- Filter notes by tags 🔎  
- Authentication and access control (each user sees only their notes) 👤  
- Simple and responsive design with Bootstrap 🎨  

---

## ⚙️ Installation and Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/USERNAME/NoteApp.git
   cd NoteApp
Create and activate a virtual environment:
python -m venv .venv
source .venv/bin/activate   # Linux/Mac
.venv\Scripts\activate      # Windows

Install dependencies:
pip install -r requirements.txt

Run database migrations:
python manage.py migrate

Start the development server:
python manage.py runserver

Open in your browser:
http://127.0.0.1:8000

📂 Project Structure
php
Копировать код
NoteApp/
│── notebook/        # main app
│── templates/       # HTML templates
│── static/          # static files (CSS, JS, Bootstrap)
│── db.sqlite3       # SQLite database
│── manage.py        # main Django management file
│── requirements.txt # project dependencies
│── README.md        # project documentation

👨‍💻 Technologies Used
Python 3.12
Django 5
Bootstrap 5

