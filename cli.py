import click

@click.group()
def audioforge():
    """Audio Forge - AI-Powered Audio Transformation CLI"""
    pass

@audioforge.command()
@click.option('--voice', help="Path to the voice sample")
@click.option('--pitch', default=1.0, help="Pitch adjustment")
@click.option('--effect', type=click.Choice(['echo', 'distortion']), help="Optional effects")
def clone(voice, pitch, effect):
    """Voice Cloning with customization"""
    if not voice:
        print("Please provide a path to the voice sample.")
        return
    
    output = clone_voice(voice, pitch, effect)
    if output:
        print(f"Voice cloning complete. Output saved to {output}.")
    else:
        print("Voice cloning failed.")

@audioforge.command()
@click.option('--audio', help="Path to the raw audio file")
def mix(audio):
    """Apply mixing and mastering to raw audio"""
    if not audio:
        print("Please provide a path to the audio file.")
        return
    
    output = mix_and_master(audio)
    if output:
        print(f"Mixing and mastering complete. Output saved to {output}.")
    else:
        print("Mixing and mastering failed.")

@audioforge.command()
@click.option('--song', help="Path to the song file")
@click.option('--tempo', default=1.0, help="Tempo adjustment factor")
@click.option('--effect', type=click.Choice(['reverb', 'echo']), help="Optional effects")
def remix(song, tempo, effect):
    """Remix a song with tempo adjustment and effects"""
    if not song:
        print("Please provide a path to the song file.")
        return
    
    output = remix_song(song, tempo, effect)
    if output:
        print(f"Remixing complete. Output saved to {output}.")
    else:
        print("Remixing failed.")
        


@audioforge.command()
@click.option('--song', help="Path to the song file")
@click.option('--modifications', type=str, help="Modifications in JSON format, e.g., '{\"intro\": \"repeat\", \"bridge\": \"remove\"}'")
def structure(song, modifications):
    """Customize song structure by rearranging sections"""
    if not song or not modifications:
        print("Please provide a song file and structure modifications.")
        return
    
    try:
        import json
        modifications_dict = json.loads(modifications)
    except json.JSONDecodeError:
        print("Invalid format for modifications. Please provide a valid JSON string.")
        return

    output = customize_structure(song, modifications_dict)
    if output:
        print(f"Structure customization complete. Output saved to {output}.")
    else:
        print("Structure customization failed.")



@audioforge.command()
@click.option('--song', help="Path to the song file")
@click.option('--language', help="Target language code (e.g., 'es' for Spanish, 'fr' for French)")
@click.option('--lyrics', help="Original lyrics (optional)")
def multilanguage(song, language, lyrics):
    """Create a multilingual version of the song by translating lyrics and adapting the beat"""
    if not song or not language:
        print("Please provide both a song file and target language.")
        return

    output = create_multilanguage_song(song, language, lyrics)
    if output:
        print(f"Multi-language music creation complete. Output saved to {output}.")
    else:
        print("Multi-language music creation failed.")


@audioforge.command()
@click.option('--song', help="Path to song for inspiration")
def inspire(song):
    """Generate new music inspired by an existing track"""
    if not song:
        print("Please provide a song file for inspiration.")
        return

    new_song_path = generate_inspired_music(song)
    
    if new_song_path:
        print(f"New music generated based on {song}. Saved to {new_song_path}.")
    else:
        print("Failed to generate new music.")

if __name__ == '__main__':
    audioforge()
