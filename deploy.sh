#!/bin/bash

echo "🎵 FreudMusic Deployment Helper 🎵"
echo "=================================="

# Check if git is initialized
if [ ! -d ".git" ]; then
    echo "❌ Git repository not found. Initializing..."
    git init
    git add .
    git commit -m "Initial commit: FreudMusic AI Techno Generator"
    echo "✅ Git repository initialized"
else
    echo "✅ Git repository found"
fi

# Build frontend to test
echo "🔨 Testing frontend build..."
cd frontend
npm run build
if [ $? -eq 0 ]; then
    echo "✅ Frontend build successful"
else
    echo "❌ Frontend build failed"
    exit 1
fi
cd ..

# Test backend
echo "🔨 Testing backend..."
cd backend
source venv/bin/activate
python3 -c "import simple_main; print('✅ Backend imports successful')"
cd ..

echo ""
echo "🚀 Ready for deployment!"
echo ""
echo "Next steps:"
echo "1. Push to GitHub: git push origin main"
echo "2. Deploy backend to Render:"
echo "   - Go to https://render.com"
echo "   - Create new Web Service"
echo "   - Connect your GitHub repo"
echo "   - Set root directory: backend"
echo "   - Set build command: pip install -r requirements.txt"
echo "   - Set start command: uvicorn simple_main:app --host 0.0.0.0 --port \$PORT"
echo ""
echo "3. Deploy frontend to Vercel:"
echo "   - Go to https://vercel.com"
echo "   - Import your GitHub repo"
echo "   - Set root directory: frontend"
echo "   - Set environment variable: VITE_API_URL=https://your-render-url.onrender.com"
echo ""
echo "📖 See DEPLOYMENT.md for detailed instructions" 