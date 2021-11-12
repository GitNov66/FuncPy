import numpy

def binary_step(x):
	if x < 0:
		return 0
	elif x >= 0:
		return 1

def sigmoid(x):
	return 1 / (1 + np.exp(-x))

def tanh(x):
	return (np.exp(x) - np.exp(-x)) / (np.exp(x) + np.exp(-x))

def ReLU(x):
	if x < 0:
		return 0
	elif x >= 0:
		return x

def softplus(x):
	return np.log(1 + np.exp(x))

def leaky_ReLU(x):
	k = 0.1

	if x < 0:
		return x * k
	elif x >= 0:
		return x
