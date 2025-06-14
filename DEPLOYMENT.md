# FreudMusic Deployment Guide

## Overview
FreudMusic is deployed using:
- **Frontend**: Vercel (React + Vite)
- **Backend**: Render (FastAPI + Python)

## Frontend Deployment (Vercel)

### Prerequisites
- GitHub repository
- Vercel account

### Steps
1. Push your code to GitHub
2. Connect your GitHub repo to Vercel
3. Configure build settings:
   - **Framework Preset**: Vite
   - **Root Directory**: `frontend`
   - **Build Command**: `npm run vercel-build`
   - **Output Directory**: `dist`

### Environment Variables
Set in Vercel dashboard:
```
VITE_API_URL=https://freudmusic-backend.onrender.com
```

## Backend Deployment (Render)

### Prerequisites
- GitHub repository
- Render account

### Steps
1. Create a new Web Service on Render
2. Connect your GitHub repository
3. Configure service:
   - **Root Directory**: `backend`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `uvicorn simple_main:app --host 0.0.0.0 --port $PORT`
   - **Python Version**: 3.8

### Environment Variables
Set in Render dashboard:
```
PORT=10000
PYTHON_VERSION=3.8.10
```

## Local Development

### Backend
```bash
cd backend
source venv/bin/activate
uvicorn simple_main:app --host 0.0.0.0 --port 8002
```

### Frontend
```bash
cd frontend
npm run dev
```

## Production URLs
- **Frontend**: https://freudmusic.vercel.app
- **Backend**: https://freudmusic-backend.onrender.com
- **API Docs**: https://freudmusic-backend.onrender.com/docs

## Testing Deployment
```bash
# Test backend
curl https://freudmusic-backend.onrender.com/status

# Test frontend
curl https://freudmusic.vercel.app
``` 