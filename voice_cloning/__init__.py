import librosa
import soundfile as sf
from pydub import AudioSegment, effects

def clone_voice(voice_path, pitch=1.0, effect=None):
    """
    Clone a voice sample, adjusting pitch and adding effects.
    
    Parameters:
    - voice_path: str - Path to the input voice sample file.
    - pitch: float - Pitch adjustment factor (e.g., 1.2 for higher pitch, 0.8 for lower).
    - effect: str - Optional effect to apply (e.g., "echo", "distortion").

    Returns:
    - output_path: str - Path to the output file with the cloned voice.
    """
    
    try:
        audio, sr = librosa.load(voice_path, sr=None)
    except Exception as e:
        print(f"Error loading audio file: {e}")
        return None
    
    if pitch != 1.0:
        audio = librosa.effects.pitch_shift(audio, sr, n_steps=pitch)

    audio_segment = AudioSegment(audio.tobytes(), frame_rate=sr, sample_width=audio.dtype.itemsize, channels=1)
    
    
    if effect == "echo":
        audio_segment = audio_segment + audio_segment.reverse()  
    elif effect == "distortion":
        audio_segment = effects.distort(audio_segment)  

    output_path = "cloned_voice.wav"
    audio_segment.export(output_path, format="wav")
    print(f"Cloned voice saved to {output_path}")
    return output_path
