import librosa

def get_mfcc(file):
	y, sr = librosa.load(file)
	return librosa.feature.melspectrogram(y=y, sr=sr)
	
def get_loudness(file):
	y, sr = librosa.load(file)
	return librosa.feature.rmse(y=y)