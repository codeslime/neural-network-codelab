import numpy as np

def sigmoid(x):
        return 1/(1+np.exp(-x))

class Neuron:
    def __init__(self, weights,bias):
        self.weights = weights
        self.bias = bias

    def feedforward(self,inputs):
        total = np.dot(self.weights,inputs) + self.bias
        return sigmoid(total)

inputs = np.array([1,0])
weights = np.array([0,1])
bias  = 4 

neuron1 = Neuron(weights,bias) 

print(neuron1.feedforward(inputs))