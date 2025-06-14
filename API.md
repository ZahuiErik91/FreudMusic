# API Documentation

## Base URL
`http://localhost:8000/`

## Endpoints

### 1. `GET /status`
- **Description:** Health check for backend and streaming pipeline.
- **Response:**
```json
{
  "status": "ok",
  "streaming": true
}
```

### 2. `POST /controls`
- **Description:** Update music generation parameters (tempo, pitch, pattern complexity, effects).
- **Request Body:**
```json
{
  "tempo": 128,
  "pitch": 0,
  "pattern_complexity": 0.5,
  "effect_levels": {
    "reverb": 0.3,
    "delay": 0.2,
    "filter_cutoff": 0.7
  }
}
```
- **Response:**
```json
{
  "success": true,
  "message": "Controls updated"
}
```

### 3. `GET /current`
- **Description:** Get current music generation parameters.
- **Response:**
```json
{
  "tempo": 128,
  "pitch": 0,
  "pattern_complexity": 0.5,
  "effect_levels": {
    "reverb": 0.3,
    "delay": 0.2,
    "filter_cutoff": 0.7
  }
}
```

## Example Usage

**Update Controls:**
```bash
curl -X POST http://localhost:8000/controls \
  -H 'Content-Type: application/json' \
  -d '{"tempo":130,"pattern_complexity":0.7}'
```

**Check Status:**
```bash
curl http://localhost:8000/status
``` 