from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

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

@app.get("/")
def root():
    return {"message": "FreudMusic API is running"}

@app.get("/status")
def get_status():
    return {"status": "ok", "streaming": state["streaming"]}

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
    
    print(f"Controls updated: tempo={controls.tempo}, pattern={controls.pattern_complexity}")
    
    return {"success": True, "message": "Controls updated"}

if __name__ == "__main__":
    import uvicorn
    import os
    port = int(os.environ.get("PORT", 8001))
    uvicorn.run(app, host="0.0.0.0", port=port) 