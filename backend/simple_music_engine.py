import threading
import time
import math
import wave
import struct
import tempfile
import os
from typing import Dict

class SimpleMusicEngine:
    def __init__(self):
        self.tempo = 128
        self.pattern_complexity = 0.5
        self.reverb = 0.3
        self.running = False
        self.thread = None
        
    def update_parameters(self, params: Dict):
        """Update music generation parameters"""
        self.tempo = params.get('tempo', self.tempo)
        self.pattern_complexity = params.get('pattern_complexity', self.pattern_complexity)
        self.reverb = params.get('effect_levels', {}).get('reverb', self.reverb)
        print(f"Music engine updated: tempo={self.tempo}, pattern={self.pattern_complexity}, reverb={self.reverb}")
    
    def generate_kick(self, sample_rate=44100, duration=0.1):
        """Generate a simple kick drum sound"""
        samples = int(sample_rate * duration)
        kick = []
        for i in range(samples):
            t = i / sample_rate
            # Simple kick: low frequency sine wave with exponential decay
            freq = 60 * (1 - t * 5)  # Frequency drops quickly
            amplitude = math.exp(-t * 20) * 0.8  # Exponential decay
            sample = amplitude * math.sin(2 * math.pi * freq * t)
            kick.append(sample)
        return kick
    
    def generate_hihat(self, sample_rate=44100, duration=0.05):
        """Generate a simple hi-hat sound"""
        samples = int(sample_rate * duration)
        hihat = []
        for i in range(samples):
            t = i / sample_rate
            # Hi-hat: filtered noise with quick decay
            noise = (hash(i) % 1000 - 500) / 500.0  # Simple noise
            amplitude = math.exp(-t * 50) * 0.3
            sample = amplitude * noise
            hihat.append(sample)
        return hihat
    
    def generate_bass(self, sample_rate=44100, duration=0.25, note_freq=55):
        """Generate a simple bass line"""
        samples = int(sample_rate * duration)
        bass = []
        for i in range(samples):
            t = i / sample_rate
            # Simple saw wave bass
            amplitude = 0.4 * (1 - t * 2)  # Decay
            sample = amplitude * (2 * (t * note_freq % 1) - 1)  # Saw wave
            bass.append(sample)
        return bass
    
    def generate_pattern(self, sample_rate=44100, pattern_length=4.0):
        """Generate a complete pattern based on current parameters"""
        samples = int(sample_rate * pattern_length)
        pattern = [0.0] * samples
        
        # Calculate timing
        beat_duration = 60.0 / self.tempo  # Duration of one beat in seconds
        sixteenth_duration = beat_duration / 4  # 16th note duration
        
        # Generate sounds
        kick = self.generate_kick(sample_rate)
        hihat = self.generate_hihat(sample_rate)
        bass = self.generate_bass(sample_rate, note_freq=55)
        
        # Place kicks (4/4 pattern)
        for beat in range(4):
            start_sample = int(beat * beat_duration * sample_rate)
            for i, sample in enumerate(kick):
                if start_sample + i < len(pattern):
                    pattern[start_sample + i] += sample
        
        # Place hi-hats (based on complexity)
        hihat_density = int(8 * self.pattern_complexity + 4)  # 4-12 hi-hats per pattern
        for i in range(hihat_density):
            start_sample = int(i * sixteenth_duration * sample_rate)
            for j, sample in enumerate(hihat):
                if start_sample + j < len(pattern):
                    pattern[start_sample + j] += sample * 0.5
        
        # Add bass line
        for beat in range(4):
            if beat % 2 == 0:  # Bass on beats 1 and 3
                start_sample = int(beat * beat_duration * sample_rate)
                for i, sample in enumerate(bass):
                    if start_sample + i < len(pattern):
                        pattern[start_sample + i] += sample
        
        # Apply simple reverb (delay + feedback)
        if self.reverb > 0:
            delay_samples = int(0.1 * sample_rate)  # 100ms delay
            for i in range(delay_samples, len(pattern)):
                pattern[i] += pattern[i - delay_samples] * self.reverb * 0.3
        
        return pattern
    
    def save_audio_chunk(self, audio_data, filename, sample_rate=44100):
        """Save audio data to a WAV file"""
        with wave.open(filename, 'w') as wav_file:
            wav_file.setnchannels(1)  # Mono
            wav_file.setsampwidth(2)  # 16-bit
            wav_file.setframerate(sample_rate)
            
            # Convert float samples to 16-bit integers
            for sample in audio_data:
                # Clamp and convert to 16-bit
                sample = max(-1.0, min(1.0, sample))
                wav_file.writeframes(struct.pack('<h', int(sample * 32767)))
    
    def music_generation_loop(self):
        """Main loop for continuous music generation"""
        print("Music generation started!")
        chunk_duration = 4.0  # 4-second chunks
        
        while self.running:
            # Generate a pattern
            pattern = self.generate_pattern(pattern_length=chunk_duration)
            
            # Save to temporary file
            temp_file = tempfile.NamedTemporaryFile(suffix='.wav', delete=False)
            temp_file.close()
            
            self.save_audio_chunk(pattern, temp_file.name)
            print(f"Generated audio chunk: {temp_file.name}")
            
            # Clean up old temp files (simple cleanup)
            try:
                os.unlink(temp_file.name)
            except:
                pass
            
            # Wait for next chunk (accounting for generation time)
            time.sleep(chunk_duration * 0.9)  # Slight overlap
    
    def start(self):
        """Start the music generation engine"""
        if not self.running:
            self.running = True
            self.thread = threading.Thread(target=self.music_generation_loop)
            self.thread.daemon = True
            self.thread.start()
            print("Music engine started")
    
    def stop(self):
        """Stop the music generation engine"""
        self.running = False
        if self.thread:
            self.thread.join()
        print("Music engine stopped")

# Global instance
music_engine = SimpleMusicEngine() 