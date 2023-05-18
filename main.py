from remove_silence import remove_silence
from splice import splice_audio
from youtube_to_wav import youtube_to_wav
import subprocess
import shutil
import os


def create_dir():
    try: 
        os.mkdir("silenced_vocals")
    except:
        pass
    
    try: 
        os.mkdir("complete_dataset")
    except:
        pass
    


directory = input('Enter the directory with urls.txt: ')


while directory not in os.listdir():
    print("\nInvalid Directory Name.")
    directory = input('Enter the directory with urls.txt: ')

os.chdir(directory)

youtube_to_wav()
create_dir()

for track in os.listdir():
    if track.endswith(".wav"):
        remove_silence(track)
        splice_audio(f"silenced_vocals/{track}")