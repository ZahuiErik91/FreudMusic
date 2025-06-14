#!/bin/bash
set -e

# 1. Backend Setup
cd backend
if [ ! -f .env ]; then
  echo ".env not found, copying from .env.example"
  cp .env.example .env
fi

if [ ! -d venv ]; then
  python3 -m venv venv
fi
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

# Launch backend
echo "Launching backend on http://localhost:8000 ..."
uvicorn main:app --reload --port 8000 &
BACKEND_PID=$!
cd ..

# 2. Frontend Setup
cd frontend
if [ ! -d node_modules ]; then
  npm install
fi

# Launch frontend with Vite
echo "Launching frontend on http://localhost:3000 ..."
npm run dev &
FRONTEND_PID=$!
cd ..

# 3. YouTube Streaming Test
# Extract stream key and URL from backend/.env
STREAM_KEY=$(grep '^YOUTUBE_STREAM_KEY=' backend/.env | cut -d '=' -f2)
STREAM_URL=$(grep '^STREAM_URL=' backend/.env | cut -d '=' -f2)

if [ -z "$STREAM_KEY" ] || [ "$STREAM_KEY" = "your_youtube_stream_key_here" ]; then
  echo "Warning: YOUTUBE_STREAM_KEY not set in backend/.env - skipping stream test"
  FFMPEG_PID=""
else
  FULL_URL="$STREAM_URL/$STREAM_KEY"
  echo "Streaming test sine wave to YouTube..."
  ffmpeg -re -f lavfi -i "sine=frequency=440:duration=3600" -f lavfi -i anullsrc -shortest -c:a aac -b:a 128k -ar 44100 -f flv "$FULL_URL" &
  FFMPEG_PID=$!
fi

# 4. Print info
cat <<EOF

---
Backend running at:   http://localhost:8000
Frontend running at:  http://localhost:3000
YouTube stream URL:   ${FULL_URL:-"Not configured"}
Check your YouTube Live Dashboard to see the test stream.
---

To stop all processes, run:
  kill $BACKEND_PID $FRONTEND_PID $FFMPEG_PID
EOF

# Wait for background jobs
wait $BACKEND_PID $FRONTEND_PID $FFMPEG_PID 