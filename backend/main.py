from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Dict
from contextlib import asynccontextmanager
from simple_music_engine import music_engine

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    music_engine.start()
    print("FreudMusic API started with music engine")
    yield
    # Shutdown
    music_engine.stop()
    print("FreudMusic API stopped")

app = FastAPI(lifespan=lifespan)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# In-memory state for music parameters
state = {
    "tempo": 128,
    "pitch": 0,
    "pattern_complexity": 0.5,
    "effect_levels": {
        "reverb": 0.3,
        "delay": 0.2,
        "filter_cutoff": 0.7
    },
    "streaming": True
}

class EffectLevels(BaseModel):
    reverb: float = 0.3
    delay: float = 0.2
    filter_cutoff: float = 0.7

class Controls(BaseModel):
    tempo: int = 128
    pitch: int = 0
    pattern_complexity: float = 0.5
    effect_levels: EffectLevels = EffectLevels()

@app.get("/status")
def get_status():
    return {"status": "ok", "streaming": state["streaming"], "music_engine": music_engine.running}

@app.get("/current")
def get_current():
    return {
        "tempo": state["tempo"],
        "pitch": state["pitch"],
        "pattern_complexity": state["pattern_complexity"],
        "effect_levels": state["effect_levels"]
    }

@app.post("/controls")
def update_controls(controls: Controls):
    state["tempo"] = controls.tempo
    state["pitch"] = controls.pitch
    state["pattern_complexity"] = controls.pattern_complexity
    state["effect_levels"] = controls.effect_levels.dict()
    
    # Update the music engine with new parameters
    music_engine.update_parameters({
        "tempo": controls.tempo,
        "pattern_complexity": controls.pattern_complexity,
        "effect_levels": controls.effect_levels.dict()
    })
    
    return {"success": True, "message": "Controls updated"} 