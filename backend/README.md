# Learning Platform - Django Backend

## Setup Instructions

1. Create a virtual environment:
```bash
python -m venv venv
```

2. Activate the virtual environment:
- Windows: `venv\Scripts\activate`
- Linux/Mac: `source venv/bin/activate`

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

5. Create a superuser:
```bash
python manage.py createsuperuser
```

6. Run the development server:
```bash
python manage.py runserver
```

The API will be available at `http://localhost:8000/api/`

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

