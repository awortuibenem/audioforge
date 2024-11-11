from pydub import AudioSegment
from googletrans import Translator 
import librosa
import numpy as np

def create_multilanguage_song(song_path, target_language, lyrics=None, output_path="multilanguage_song.wav"):
    """
    Recreate a song in a different language with adapted lyrics and beat.
    
    Parameters:
    - song_path: str - Path to the original song file.
    - target_language: str - Target language code (e.g., 'es' for Spanish, 'fr' for French).
    - lyrics: str - Original lyrics (optional). If not provided, placeholder lyrics will be used.
    - output_path: str - Path to save the newly created multilingual song.
    
    Returns:
    - output_path: str - Path to the output file with the new song in the target language.
    """
    
    translator = Translator()
    translated_lyrics = None
    if lyrics:
        translated_lyrics = translator.translate(lyrics, dest=target_language).text
    else:
        translated_lyrics = "Placeholder lyrics for translation" 
        
    try:
        song, sr = librosa.load(song_path, sr=None)
    except Exception as e:
        print(f"Error loading song file: {e}")
        return None
    
    
    language_tempo_mapping = {
        "es": 1.1,  
        "fr": 1.0,  
        "jp": 0.9   
    }
    tempo_factor = language_tempo_mapping.get(target_language, 1.0)  
    
    
    modified_song = librosa.effects.time_stretch(song, tempo_factor)
    
    
    modified_song_segment = AudioSegment(
        np.int16(modified_song * 32767).tobytes(),
        frame_rate=sr,
        sample_width=2,  
        channels=1
    )
    
    
    print(f"Translated lyrics in {target_language}: {translated_lyrics}")
    
    modified_song_segment.export(output_path, format="wav")
    print(f"Multi-language song saved to {output_path}")
    return output_path
