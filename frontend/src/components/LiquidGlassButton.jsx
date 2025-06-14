import React from 'react'

/**
 * LiquidGlassButton - Minimal, glassy button for main UI interaction.
 * Inspired by Yeezy.com and the provided 3D/blurred glass effect.
 *
 * Props:
 * - children: Button label or content
 * - onClick: Click handler
 */
export default function LiquidGlassButton({ children, onClick }) {
  return (
    <button
      onClick={onClick}
      style={{
        padding: '1.2em 2.5em',
        borderRadius: '2em',
        border: 'none',
        background: 'rgba(255,255,255,0.25)',
        boxShadow: '0 4px 32px rgba(0,0,0,0.12)',
        backdropFilter: 'blur(12px)',
        WebkitBackdropFilter: 'blur(12px)',
        color: '#111',
        fontSize: '1.2em',
        fontWeight: 600,
        letterSpacing: '0.05em',
        cursor: 'pointer',
        transition: 'background 0.2s',
      }}
    >
      {children}
    </button>
  )
} 