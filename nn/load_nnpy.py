import numpy 
from keras.models import load_model
#from keras.layers import Dense
from numpy import loadtxt


# load model
model = load_model('model.h5')
# summarize model
model.summary()
# load dataset
dataset = loadtxt('solarpanel_data.csv', delimiter=',')
# split into input (X) and output (y) variables
X = dataset[:,0:8]
y = dataset[:,8]
# evaluate the model
scores = model.evaluate(X, y, verbose = 0)
print("%S: %.2f%%" %(model.matrics_names[1], scores[1]*100))


