import React, { useState, useEffect } from 'react'
import LiquidGlassButton from './components/LiquidGlassButton'

export default function App() {
  const [tempo, setTempo] = useState(128)
  const [pattern, setPattern] = useState(0.5)
  const [reverb, setReverb] = useState(0.3)
  const [status, setStatus] = useState('disconnected')
  
  const API_BASE = import.meta.env.VITE_API_URL || 'http://localhost:8002'

  // Load current settings from backend on mount
  useEffect(() => {
    fetch(`${API_BASE}/current`)
      .then(res => res.json())
      .then(data => {
        setTempo(data.tempo)
        setPattern(data.pattern_complexity)
        setReverb(data.effect_levels.reverb)
        setStatus('connected')
      })
      .catch(() => setStatus('error'))
  }, [])

  // Send controls to backend
  const handleSend = async () => {
    try {
      const response = await fetch(`${API_BASE}/controls`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          tempo,
          pattern_complexity: pattern,
          effect_levels: { reverb, delay: 0.2, filter_cutoff: 0.7 }
        })
      })
      const result = await response.json()
      setStatus(result.success ? 'updated' : 'error')
      setTimeout(() => setStatus('connected'), 2000)
    } catch (error) {
      setStatus('error')
    }
  }

  return (
    <div style={{
      minHeight: '100vh',
      display: 'flex',
      flexDirection: 'column',
      alignItems: 'center',
      justifyContent: 'center',
      background: '#d8d7d7',
    }}>
      <h1 style={{ fontWeight: 700, fontSize: '2.5em', marginBottom: '0.5em', letterSpacing: '-0.03em' }}>freudmusic</h1>
      <div style={{ fontSize: '0.9em', marginBottom: '2em', color: status === 'connected' ? '#666' : status === 'updated' ? '#0a0' : '#a00' }}>
        {status === 'connected' && '● live'}
        {status === 'updated' && '● updated'}
        {status === 'error' && '● connection error'}
        {status === 'disconnected' && '○ connecting...'}
      </div>
      
      <div style={{ display: 'flex', gap: '2em', marginBottom: '2em' }}>
        <div style={{ textAlign: 'center' }}>
          <label style={{ fontWeight: 500, display: 'block', marginBottom: '0.5em' }}>Tempo</label>
          <input type="range" min="120" max="140" value={tempo} onChange={e => setTempo(Number(e.target.value))} />
          <div style={{ fontSize: '0.9em', marginTop: '0.3em' }}>{tempo} BPM</div>
        </div>
        <div style={{ textAlign: 'center' }}>
          <label style={{ fontWeight: 500, display: 'block', marginBottom: '0.5em' }}>Pattern</label>
          <input type="range" min="0" max="1" step="0.01" value={pattern} onChange={e => setPattern(Number(e.target.value))} />
          <div style={{ fontSize: '0.9em', marginTop: '0.3em' }}>{pattern.toFixed(2)}</div>
        </div>
        <div style={{ textAlign: 'center' }}>
          <label style={{ fontWeight: 500, display: 'block', marginBottom: '0.5em' }}>Reverb</label>
          <input type="range" min="0" max="1" step="0.01" value={reverb} onChange={e => setReverb(Number(e.target.value))} />
          <div style={{ fontSize: '0.9em', marginTop: '0.3em' }}>{reverb.toFixed(2)}</div>
        </div>
      </div>
      
      <LiquidGlassButton onClick={handleSend}>Update Groove</LiquidGlassButton>
    </div>
  )
} 