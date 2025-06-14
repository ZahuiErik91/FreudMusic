# 🎵 FreudMusic - Complete Deployment Guide

## ✅ Project Status
- **GitHub Repository**: [https://github.com/ZahuiErik91/FreudMusic](https://github.com/ZahuiErik91/FreudMusic)
- **Local Development**: ✅ Working (Backend: localhost:8002, Frontend: localhost:3000)
- **Build Process**: ✅ Tested and working
- **Deployment Ready**: ✅ All configurations in place

## 🚀 Quick Deploy Instructions

### 1. Deploy Backend to Render

1. **Go to [Render.com](https://render.com)** and sign in
2. **Create New Web Service**
3. **Connect GitHub Repository**: `ZahuiErik91/FreudMusic`
4. **Configure Service**:
   - **Name**: `freudmusic-backend`
   - **Root Directory**: `backend`
   - **Environment**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `uvicorn simple_main:app --host 0.0.0.0 --port $PORT`
   - **Instance Type**: Free tier is sufficient for testing

5. **Environment Variables** (Optional):
   ```
   PYTHON_VERSION=3.8.10
   ```

6. **Deploy** - Render will automatically build and deploy

### 2. Deploy Frontend to Vercel

1. **Go to [Vercel.com](https://vercel.com)** and sign in
2. **Import Project** from GitHub: `ZahuiErik91/FreudMusic`
3. **Configure Project**:
   - **Framework Preset**: `Vite`
   - **Root Directory**: `frontend`
   - **Build Command**: `npm run vercel-build` (auto-detected)
   - **Output Directory**: `dist` (auto-detected)

4. **Environment Variables**:
   ```
   VITE_API_URL=https://freudmusic-backend.onrender.com
   ```
   *(Replace with your actual Render URL after backend deployment)*

5. **Deploy** - Vercel will automatically build and deploy

## 🔧 Local Development

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

## 📋 Project Structure

```
FreudMusic/
├── backend/                 # FastAPI backend
│   ├── simple_main.py      # Main API server
│   ├── requirements.txt    # Python dependencies
│   ├── render.yaml        # Render deployment config
│   └── venv/              # Virtual environment
├── frontend/               # React + Vite frontend
│   ├── src/
│   │   ├── App.jsx        # Main React component
│   │   ├── main.jsx       # Entry point
│   │   └── components/    # UI components
│   ├── package.json       # Node dependencies
│   ├── vite.config.js     # Vite configuration
│   └── vercel.json        # Vercel deployment config
├── DEPLOYMENT.md          # Detailed deployment guide
├── deploy.sh             # Deployment helper script
└── README.md             # Project documentation
```

## 🎛️ Features

### Backend API Endpoints
- `GET /` - API status
- `GET /status` - Service health check
- `GET /current` - Current music parameters
- `POST /controls` - Update music parameters

### Frontend Features
- **Liquid Glass Button** - Yeezy.com inspired design
- **Real-time Controls**:
  - Tempo slider (120-140 BPM)
  - Pattern complexity (0-1)
  - Reverb level (0-1)
- **Live Status Indicator** - Shows connection status
- **Responsive Design** - Works on all devices

## 🔗 Expected URLs (After Deployment)

- **Frontend**: `https://freudmusic.vercel.app`
- **Backend**: `https://freudmusic-backend.onrender.com`
- **API Documentation**: `https://freudmusic-backend.onrender.com/docs`

## 🧪 Testing Deployment

### Test Backend
```bash
curl https://freudmusic-backend.onrender.com/status
# Expected: {"status":"ok","streaming":true}
```

### Test Frontend
Visit your Vercel URL and verify:
- ✅ Page loads with "freudmusic" title
- ✅ Three sliders (Tempo, Pattern, Reverb)
- ✅ Liquid glass "Update Groove" button
- ✅ Status shows "● live" (green)

## 🎵 Next Steps (Future Enhancements)

1. **Add Music Engine**: Integrate the full music generation system
2. **YouTube Streaming**: Set up RTMP streaming to YouTube Live
3. **Audio Visualization**: Add real-time audio waveforms
4. **User Presets**: Save and load custom settings
5. **Mobile App**: React Native version

## 🆘 Troubleshooting

### Common Issues

**Backend not starting on Render:**
- Check build logs for Python dependency issues
- Verify `requirements.txt` is in backend directory
- Ensure start command uses `$PORT` environment variable

**Frontend not connecting to backend:**
- Verify `VITE_API_URL` environment variable in Vercel
- Check CORS settings in backend
- Ensure backend is deployed and accessible

**Build failures:**
- Run `./deploy.sh` locally to test build process
- Check Node.js version compatibility
- Verify all dependencies are listed in package.json

## 📞 Support

For issues or questions:
1. Check the deployment logs in Render/Vercel dashboards
2. Test locally using the development commands above
3. Review the detailed `DEPLOYMENT.md` guide 