# Deployment Guide

## Backend Deployment on Render.com

### Prerequisites
- GitHub account with repository access
- Render.com account (free tier available)

### Step-by-Step Deployment

#### 1. Connect GitHub to Render
- Go to https://render.com
- Sign up/Login with GitHub
- Authorize Render to access your repositories

#### 2. Create a Web Service
- Click **"New +"** → **"Web Service"**
- Select `learning-platform` repository
- Click **"Connect"**

#### 3. Configure Service Settings
Fill in the following:

| Field | Value |
|-------|-------|
| **Name** | learning-platform-backend |
| **Environment** | Python 3 |
| **Region** | Choose closest to you |
| **Branch** | main |
| **Build Command** | `bash build.sh` |
| **Start Command** | `cd backend && gunicorn learning_platform.wsgi:application --bind 0.0.0.0:$PORT` |

#### 4. Add Environment Variables
Click **"Advanced"** and add these variables:

```
DEBUG=False
SECRET_KEY=your-new-secure-random-key-here
ALLOWED_HOSTS=.onrender.com,learning-platform-three-rho.vercel.app
```

**Generate a secure SECRET_KEY:**
Run in Python: `python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'`

#### 5. Deploy
- Click **"Create Web Service"**
- Render will automatically build and deploy
- You'll get a URL like: `https://learning-platform-backend.onrender.com`

### Step 6: Update Frontend

Add to your Vercel environment variables:
```
REACT_APP_API_BASE_URL=https://learning-platform-backend.onrender.com/api
```

Or update `.env.local`:
```
REACT_APP_API_BASE_URL=https://your-backend-url.onrender.com/api
```

### Step 7: Test Connection

Your frontend at `learning-platform-three-rho.vercel.app` will now connect to your backend.

### Automatic Deployments

Every time you push to GitHub's `main` branch, Render will automatically:
1. Pull the latest code
2. Run migrations
3. Collect static files
4. Restart the service

### Troubleshooting

**503 Service Unavailable:**
- Check Render logs: Click service → "Logs"
- Common issues:
  - Missing environment variables
  - Failed migrations
  - Incorrect SECRET_KEY

**CORS Errors:**
- Add your frontend URL to `CORS_ALLOWED_ORIGINS` in settings.py
- Redeploy

**Database Issues:**
- Render provides SQLite (OK for small projects)
- For production, upgrade to PostgreSQL database

## Frontend Deployment (Already Done on Vercel)

Your frontend is already deployed at: `https://learning-platform-three-rho.vercel.app`

Just update the API URL in environment variables and redeploy.

---

**After Deployment:**
- Backend: `https://learning-platform-backend.onrender.com`
- Frontend: `https://learning-platform-three-rho.vercel.app`
- API calls will automatically route to the backend
