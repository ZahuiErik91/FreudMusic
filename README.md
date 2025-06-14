# FreudMusic: 24/7 AI Techno/Ambient Generator

## Overview
FreudMusic is an AI-powered, nonstop techno and ambient music generator that streams live 24/7 to YouTube. It features a super-minimal, Yeezy.com-inspired frontend with a liquid glass button, and a backend that generates and streams music in real time.

## Features
- Real-time AI/algorithmic techno & ambient music generation
- Drum machine, synths, basslines, effects, and arrangement
- Minimal, beautiful frontend with liquid glass button
- User controls for tempo, pattern complexity, and effects
- 24/7 live streaming to YouTube

## Directory Structure
```
freudmusic/
  backend/         # Music generation engine, streaming logic, API
  frontend/        # Minimal web UI (React), liquid glass button
  README.md        # This file
  PRODUCT.md       # Product vision, goals, user stories
  API.md           # API documentation
```

## Setup

### Prerequisites
- Node.js (for frontend)
- Python 3.8+ (for backend)
- FFmpeg (for streaming)
- YouTube account with streaming enabled

### Backend
1. `cd backend`
2. Install dependencies: `pip install -r requirements.txt`
3. Configure YouTube stream key in `.env`
4. Run backend: `python music_engine.py`

### Frontend
1. `cd frontend`
2. Install dependencies: `npm install`
3. Start dev server: `npm start`

### Streaming
- The backend will automatically start streaming to YouTube if configured.

## Usage
- Open the frontend in your browser.
- Use the liquid glass button and controls to tweak music parameters.
- The backend generates and streams music live.

## Contribution
Pull requests are welcome! See `GUIDELINES.md` in each directory for standards. 