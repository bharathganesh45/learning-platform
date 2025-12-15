# Learning Platform - React Frontend

## Setup Instructions

1. Install dependencies:
```bash
npm install
```

2. Start the development server:
```bash
npm start
```

The app will be available at `http://localhost:3000`

## Features

- User authentication (Login/Register)
- Course browsing and filtering
- Course enrollment
- Progress tracking
- Lesson viewer with video support
- User dashboard
- Responsive design

## Project Structure

```
src/
  ├── components/     # Reusable components
  ├── contexts/       # React contexts (Auth)
  ├── pages/          # Page components
  ├── services/       # API services
  └── App.js          # Main app component
```

## API Integration

The frontend connects to the Django backend API at `http://localhost:8000/api/`

Make sure the Django backend is running before starting the React app.

