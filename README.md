📘 Learning Platform

A full-stack online learning platform that enables users to browse courses, enroll, and interact with educational content through a modern responsive web interface.

This project contains separate frontend and backend codebases to keep concerns clean and scalable.

🧠 Project Overview

This repository implements a complete online learning system where users can:

Browse available courses

Sign up and log in

View course details

Enroll in and access courses

(Add more features that you’ve implemented — quizzes, progress tracking, admin panel, etc.)

It’s structured as a decoupled frontend + backend application to follow modern best practices in web development.

🛠 Technologies Used

Frontend: React (or Vue/Angular — update if different)
Backend: Node.js + Express (or Django/Flask/Rails — if different)
Database: MongoDB (or PostgreSQL/MySQL — update if different)
Authentication: JWT (or session-based)
Styling: CSS / Tailwind / Bootstrap

(Adjust the above to match your stack.)

📁 Folder Structure
learning-platform/
├── frontend/      # Client application
├── backend/       # API server
├── .gitignore
└── README.md

🚀 Features

✔ User authentication (signup & login)
✔ Course listing & details
✔ Enroll in courses
✔ Secure backend with RESTful APIs
✔ Responsive UI for mobile and desktop

(Customize with real features you included — e.g., search, video streaming, quizzes, payment integration.)

📥 Installation & Setup
1. Clone the repository
git clone https://github.com/bharathganesh45/learning-platform.git
cd learning-platform

2. Backend Setup
cd backend
npm install            # or pip install -r requirements.txt if your backend is Python
# Create .env with your secrets and DB connection
npm start              # or python manage.py runserver


Expected backend URLs:

http://localhost:5000 (Node/Express default)

http://localhost:8000 (Django/Flask default)

3. Frontend Setup
cd ../frontend
npm install
npm start


Frontend usually runs on:

http://localhost:3000

📌 API Endpoints (Example)
Method	Endpoint	Description
GET	/api/courses	List courses
GET	/api/courses/:id	Course details
POST	/api/users/login	User login
POST	/api/users/signup	User registration
POST	/api/enroll	Enroll in course

(Update based on your actual routes and functionality.)

🎯 How to Use

Start backend and frontend

Open the application in the browser

Register or log in

Browse courses

Enroll and begin learning

📦 Environment Variables

Create a .env file in:

backend/.env

PORT=5000
DB_URI=your_database_connection_string
JWT_SECRET=your_jwt_secret




npm test
