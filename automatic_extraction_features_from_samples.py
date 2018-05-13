import librosa
import pickle

"""
Assuming the audio files from where you'll extract are in wav format (.wav)
Assuming there are in the \Samples folder*
Assuming samples names are formed like "output<number>.wav", where number is an int*
Assuming you have 2 folders \mfcc and \loudness to store the extracted features*
Assuming the computer where you'll run this script has :
    python 3.X
    librosa 0.6.0 installed
    audio-read up-to-date
    pickle installed (ideally up-to-date too)
Extracted features are stored in files, with pickle, to send them to an environment where they will be used as learning
    
* : you can always manually change it in the code
"""

# ad hoc function to extract mfcc and loudness and return them
def my_own_extract_mfcc_loudness(filename):
    data, soundrate = librosa.load(filename,sr=None)
    tmp_mfcc = librosa.feature.melspectrogram(y=data, sr=soundrate)
    tmp_loudness = librosa.feature.rmse(y=data)
    return tmp_mfcc,tmp_loudness

# all the base name for folder and files
base_name_load_samples = "Samples\\out"
base_name_save_mfcc = "mfcc\\out"
base_name_save_loudness = "loudness\\out"

number_files_to_extract = 814

for i in range(0,number_files_to_extract):
    file_to_load = base_name_load_samples + str(i) +".wav"
    my_mfcc, my_loudness = my_own_extract_mfcc_loudness(file_to_load)
    pickle.dump(my_mfcc, open(base_name_save_mfcc + str(i) + ".txt","wb+"))
    pickle.dump(my_loudness, open(base_name_save_loudness + str(i) + ".txt","wb+"))
print("Extraction completed")