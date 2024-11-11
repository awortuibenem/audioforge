import librosa
from pydub import AudioSegment

def customize_structure(song_path, modifications, output_path="customized_song.wav"):
    """
    Modify the structure of a song by rearranging segments like intro, outro, or bridge.
    
    Parameters:
    - song_path: str - Path to the original song file.
    - modifications: dict - Dictionary specifying sections and actions (e.g., {'intro': 'repeat', 'bridge': 'remove'}).
    - output_path: str - Path to save the restructured song.
    
    Returns:
    - output_path: str - Path to the output file with the customized song structure.
    """
    # Load the song
    try:
        song, sr = librosa.load(song_path, sr=None)
    except Exception as e:
        print(f"Error loading song file: {e}")
        return None

    beats = librosa.beat.beat_track(y=song, sr=sr)[1]
    sections = list(zip(beats[:-1], beats[1:]))  
    song_segment = AudioSegment(song.tobytes(), frame_rate=sr, sample_width=song.dtype.itemsize, channels=1)


    processed_segments = []
    for start, end in sections:
        segment = song_segment[start * 1000 // sr:end * 1000 // sr]  
        
        
        if 'intro' in modifications and modifications['intro'] == 'repeat':
            processed_segments.append(segment)  
        elif 'bridge' in modifications and modifications['bridge'] == 'remove':
            continue 
        else:
            processed_segments.append(segment)  
            
    customized_song = sum(processed_segments)
    customized_song.export(output_path, format="wav")
    print(f"Customized song saved to {output_path}")
    return output_path
