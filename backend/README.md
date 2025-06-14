# FreudMusic Backend

## Overview
Python backend for AI-driven techno/ambient music generation and 24/7 YouTube streaming.

## Setup
1. `pip install -r requirements.txt`
2. Copy `.env.example` to `.env` and fill in your YouTube stream key
3. `uvicorn main:app --reload`

## API
- See `../API.md` for endpoint documentation

## Streaming
- Music generation and streaming logic is stubbed in `music_engine.py` and `stream_to_youtube.py`
- Configure your YouTube stream key and RTMP URL in `.env` 