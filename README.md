📘 Django Social Media Platform

A simple Social Media Web Application built using Python and Django.
This project allows users to create posts, like posts, and comment on posts.

It demonstrates the basics of web application development and backend functionality using Django.

🚀 Features

✨ User Login & Logout
📝 Create Posts
❤️ Like Posts
💬 Comment on Posts
📊 Dashboard to view all posts

🛠️ Technologies Used

🐍 Python

🌐 Django Framework

🗄️ SQLite Database

🎨 HTML

🎨 CSS

⚡ Bootstrap (for UI)

📂 Project Structure
social_project/
│
├── manage.py
├── social_project/
│
├── posts/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│
├── templates/
│   ├── base.html
│   ├── dashboard.html
│   ├── login.html
│
└── db.sqlite3
⚙️ Installation Guide (Step by Step)

Follow these steps to run the project locally.

1️⃣ Clone the Repository
git clone https://github.com/yourusername/django-social-media.git
2️⃣ Go to Project Directory
cd django-social-media
3️⃣ Create Virtual Environment
python -m venv venv
4️⃣ Activate Virtual Environment
Windows
venv\Scripts\activate
Linux / Mac
source venv/bin/activate
5️⃣ Install Dependencies
pip install django
6️⃣ Run Migrations
python manage.py makemigrations
python manage.py migrate
7️⃣ Create Admin User
python manage.py createsuperuser

Enter:

Username
Email
Password
8️⃣ Run the Server
python manage.py runserver
9️⃣ Open in Browser
http://127.0.0.1:8000
👤 How to Use the Application

1️⃣ Register or login to the application
2️⃣ Create a new post
3️⃣ View posts from the dashboard
4️⃣ Like posts
5️⃣ Comment on posts

🎯 Learning Objectives

This project helps understand:

Django Models

Django Views

Django Templates

URL Routing

Database migrations

Authentication system

📌 Future Improvements

🔹 User profiles
🔹 Friend system
🔹 Image upload in posts
🔹 Real-time notifications
🔹 REST API for mobile apps
