import numpy 
from keras.models import Sequential
from keras.layers import Dense
from keras.models import model_from_json
import os
# load the dataset
dataset = loadtxt('solarpanel_data.csv', delimiter=',')
# split into input (X) and output (y) variables
X = dataset[:,0:8]
y = dataset[:,8]
# define the keras model
model = Sequential()
model.add(Dense(12, input_dim=8, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='sigmoid'))
# compile the keras model
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
# fit the keras model on the dataset
model.fit(X, y, epochs=150, batch_size=10, verbose=0)
# make class predictions with the model
#predictions = model.predict_classes(X)
# summarize the first 5 cases
#for i in range(5):
#	print('%s => %d (expected %d)' % (X[i].tolist(), predictions[i], y[i]))
scores = model.evaluate(X, y, verbose = 0)
print("%S: %.2f%%" %(model.matrics_names[1], scores[1]*100))

#seralize model to JSON
model_json = model.to_json()
with open("model.json", "w") as json_file:
	json_file.write(model.json)
#seralize model to JSON
model.save_weights("model.h5")
print("Saved model to disk")

#later...

# load json and create model
json_file = open('model.json', 'r')
loaded_model_json = json_file.read()
jsonfile.close()
loaded_model = model_from_json(loaded_model_json)
# load weights into new model
loaded_model.load_weights("model.h5")
print("loaded model from disk")

# evaluate loaded model on test data
loaded_model.compile(loss = 'binary_crossentropy', optimizer='rmsprop', metrics=['accuracy'])	
