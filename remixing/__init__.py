import librosa
from pydub import AudioSegment, effects

def remix_song(song_path, tempo=1.0, effect=None, output_path="remixed_song.wav"):
    """
    Apply remixing effects to a song, including tempo change and optional effects.
    
    Parameters:
    - song_path: str - Path to the original song file.
    - tempo: float - Tempo adjustment factor (e.g., 1.2 to speed up, 0.8 to slow down).
    - effect: str - Optional effect to apply (e.g., "reverb", "echo").
    - output_path: str - Path to save the remixed song.

    Returns:
    - output_path: str - Path to the output file with the remixed song.
    """
    
    try:
        audio, sr = librosa.load(song_path, sr=None)
    except Exception as e:
        print(f"Error loading song file: {e}")
        return None

    if tempo != 1.0:
        audio = librosa.effects.time_stretch(audio, rate=tempo)

    audio_segment = AudioSegment(audio.tobytes(), frame_rate=sr, sample_width=audio.dtype.itemsize, channels=1)
    
    
    if effect == "reverb":
        audio_segment = effects.normalize(audio_segment)  
    elif effect == "echo":
        audio_segment = audio_segment + audio_segment.reverse()  


    audio_segment.export(output_path, format="wav")
    print(f"Remixed song saved to {output_path}")
    return output_path
