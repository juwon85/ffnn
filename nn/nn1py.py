import numpy 
from keras.models import Sequential
from keras.layers import Dense
from numpy import loadtxt

# load the dataset
dataset = loadtxt('solarpanel_data.csv', delimiter=',')
# split into input (X) and output (y) variables
X = dataset[:,0:4]
y = dataset[:,4: ]
# define the keras model
model = Sequential()
model.add(Dense(8, input_dim=4, activation='relu'))
model.add(Dense(4, activation='relu'))
model.add(Dense(2, activation='sigmoid'))
# compile the keras model
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
# fit the keras model on the dataset
model.fit(X, y, epochs=80, batch_size=8, verbose=0)
# make class predictions with the model
#predictions = model.predict_classes(X)
# summarize the first 5 cases
#for i in range(5):
#	print('%s => %d (expected %d)' % (X[i].tolist(), predictions[i], y[i]))
scores = model.evaluate(X, y, verbose = 0)
print("%s: %.2f%%" %(model.metrics_names[1], scores[1]*100))
# save model and architecture to single file
model.save("model.h5")
print("saved model to disk")

