import librosa

def get_mfcc(file):
	#return the mfcc array of an audio file
	data, soundrate = librosa.load(file)
	return librosa.feature.melspectrogram(y=data, sr=soundrate)
	
def get_loudness(file):
	#return the loudness array of an audio file
	data, soundrate = librosa.load(file)
	return librosa.feature.rmse(y=data)