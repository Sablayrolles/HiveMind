import keras

mfcc_conv_pool_2D = 1;
loudness_conv_pool_2D = 1;
mfcc_conv_pool_1D = 1;
loudness_conv_pool_1D = 1;
fnn_dense = 1;

class Model:
	def __init__(self):
		self.model = None
		
	def summary(self):
		print(self.model.summary())
		
	def to_img(self, file):
		keras.utils.plot_model(self.model, to_file=file+'.png', show_shapes=True)
		
	def get(self):
		return self.model

class Model_mfcc(Model):
	def __init__(self, mfcc_conv_pool_2D, mfcc_conv_pool_1D) :
		self.mfcc_conv_pool_2D = mfcc_conv_pool_2D
		self.mfcc_conv_pool_1D = mfcc_conv_pool_1D
		
	def build(self) :
		self.model = keras.models.Sequential()
		for i in range(self.mfcc_conv_pool_2D)
			self.model.add(keras.layers.Conv2D())
			self.model.add(keras.layers.AveragePooling2D())
			
		for i in range(self.mfcc_conv_pool_1D)
			self.model.add(keras.layers.Conv2D())
			self.model.add(keras.layers.AveragePooling2D())
		
		# For a binary classification problem
		self.model.compile(optimizer='rmsprop',
              loss='binary_crossentropy',
              metrics=['accuracy'])
			  
class Model_loudness(Model):
	def __init__(self, loudness_conv_pool_2D, loudness_conv_pool_1D) :
		self.loudness_conv_pool_2D = loudness_conv_pool_2D
		self.loudness_conv_pool_1D = loudness_conv_pool_1D
		
	def build(self) :
		self.model = keras.models.Sequential()
		for i in range(self.loudness_conv_pool_2D)
			self.model.add(keras.layers.Conv2D())
			self.model.add(keras.layers.MaxPooling2D())
			
		for i in range(self.loudness_conv_pool_1D)
			self.model.add(keras.layers.Conv2D())
			self.model.add(keras.layers.MaxPooling1D())
		
		# For a binary classification problem
		self.model.compile(optimizer='rmsprop',
              loss='binary_crossentropy',
              metrics=['accuracy'])
			  
class Model_FNN(Model):
	def __init__(self, model_MFCC, model_loudness, fnn_dense):
		self.model_MFCC = model_MFCC
		self.model_loudness = model_loudness
		self.fnn_dense = fnn_dense
		
	def build(self):
		self.model = keras.models.Sequential()
		self.model.add(model_MFCC)
		self.model.add(model_loudness)
		for i in range(self.fnn_dense):
			self.model.add(keras.layers.Dense())
		self.model.add(keras.layers.Dropout())