# Learning Platform

A complete learning platform built with React and Django, featuring course management, user authentication, enrollment system, and progress tracking.

## Features

### Backend (Django)
- RESTful API with Django REST Framework
- JWT authentication
- User management (students and instructors)
- Course and lesson management
- Enrollment system
- Progress tracking
- Category system
- Image upload support

### Frontend (React)
- Modern, responsive UI
- User authentication (Login/Register)
- Course browsing with filters
- Course detail pages
- Enrollment functionality
- User dashboard
- Lesson viewer with video support
- Progress tracking visualization

## Project Structure

```
learning platform/
├── backend/          # Django backend
│   ├── courses/      # Course app
│   ├── users/        # User app
│   └── learning_platform/  # Django project settings
└── frontend/         # React frontend
    └── src/
        ├── components/
        ├── contexts/
        ├── pages/
        └── services/
```

## Setup Instructions

### Backend Setup

1. Navigate to the backend directory:
```bash
cd backend
```

2. Create a virtual environment:
```bash
python -m venv venv
```

3. Activate the virtual environment:
- Windows: `venv\Scripts\activate`
- Linux/Mac: `source venv/bin/activate`

4. Install dependencies:
```bash
pip install -r requirements.txt
```

5. Run migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

6. Create a superuser:
```bash
python manage.py createsuperuser
```

7. Run the development server:
```bash
python manage.py runserver
```

The API will be available at `http://localhost:8000/api/`

### Frontend Setup

1. Navigate to the frontend directory:
```bash
cd frontend
```

2. Install dependencies:
```bash
npm install
```

3. Start the development server:
```bash
npm start
```

The app will be available at `http://localhost:3000`

## Usage

1. Start both the Django backend and React frontend servers
2. Visit `http://localhost:3000` in your browser
3. Register a new account or login
4. Browse courses and enroll in courses
5. Track your progress in the dashboard

## API Endpoints

### Authentication
- `POST /api/auth/register/` - Register a new user
- `POST /api/auth/login/` - Login
- `GET /api/auth/profile/` - Get current user profile
- `POST /api/auth/token/refresh/` - Refresh JWT token

### Courses
- `GET /api/courses/` - List all published courses
- `GET /api/courses/{id}/` - Get course details
- `POST /api/courses/{id}/enroll/` - Enroll in a course
- `GET /api/courses/{id}/my_enrollment/` - Get enrollment status

### Enrollments
- `GET /api/enrollments/` - Get user's enrollments

### Progress
- `GET /api/progress/` - Get user's progress
- `POST /api/progress/` - Update lesson progress

### Categories
- `GET /api/categories/` - List all categories

## Technologies Used

### Backend
- Django 4.2
- Django REST Framework
- JWT Authentication
- SQLite (default, can be changed to PostgreSQL/MySQL)

### Frontend
- React 18
- React Router
- Axios
- CSS3

## Development Notes

- The backend uses SQLite by default. For production, consider using PostgreSQL or MySQL
- CORS is configured to allow requests from `http://localhost:3000`
- JWT tokens are stored in localStorage
- Image uploads are stored in the `media/` directory

## License

This project is open source and available for educational purposes.

