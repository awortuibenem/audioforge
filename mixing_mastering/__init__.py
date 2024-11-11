import librosa
import soundfile as sf
from pydub import AudioSegment, effects

def mix_and_master(audio_path, output_path="mixed_and_mastered.wav"):
    """
    Apply basic mixing and mastering to an audio file.
    
    Parameters:
    - audio_path: str - Path to the input raw audio file.
    - output_path: str - Path to save the processed output file.
    
    Returns:
    - output_path: str - Path to the output file with the mixed and mastered audio.
    """
    
    try:
        audio, sr = librosa.load(audio_path, sr=None)
    except Exception as e:
        print(f"Error loading audio file: {e}")
        return None

    audio_segment = AudioSegment(audio.tobytes(), frame_rate=sr, sample_width=audio.dtype.itemsize, channels=1)
    audio_segment = effects.normalize(audio_segment) 

   
    audio_segment.export(output_path, format="wav")
    print(f"Mixed and mastered audio saved to {output_path}")
    return output_path
