from pydub import AudioSegment
from pydub.utils import make_chunks

def splice_audio(file_path):
    myaudio = AudioSegment.from_file(file_path , "wav") 
    chunk_length_ms = 10000 # pydub calculates in millisec
    chunks = make_chunks(myaudio, chunk_length_ms) #Make chunks of one sec

    file_name = file_path.split('/')[-1]

    #Export all of the individual chunks as wav files

    for i, chunk in enumerate(chunks):
        if i < (len(chunks)-1):
            chunk_name = f"{file_name}_chunk_{i}.wav"
            print("exporting", chunk_name)
            chunk.export(f"complete_dataset/{chunk_name}", format="wav")