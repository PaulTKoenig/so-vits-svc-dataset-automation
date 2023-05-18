from pydub import AudioSegment
from pydub.silence import split_on_silence

def remove_silence(file_path):
    file_name = file_path.split('/')[-1]
    audio_format = "wav"

    # Reading and splitting the audio file into chunks
    sound = AudioSegment.from_file(file_path, format = audio_format)
    audio_chunks = split_on_silence(sound
                                ,min_silence_len = 100
                                ,silence_thresh = -45
                                ,keep_silence = False
                            )

    # Putting the file back together
    combined = AudioSegment.empty()
    for chunk in audio_chunks:
        combined += chunk
    combined.export(f'silenced_vocals/{file_name}', format = audio_format)