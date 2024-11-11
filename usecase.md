Clone: python cli.py clone --voice path/to/sample.wav --pitch 1.2 --effect echo

Mixing: python cli.py mix --audio path/to/raw_audio.wav

Remix: python cli.py remix --song path/to/song.wav --tempo 1.2 --effect reverb

Structure: python cli.py structure --song path/to/song.wav --modifications '{"intro": "repeat", "bridge": "remove"}'

python cli.py multilanguage --song path/to/song.wav --language 'es' --lyrics "Original English lyrics"

python cli.py inspire --song path/to/original_song.wav
