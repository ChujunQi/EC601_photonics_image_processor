
import numpy as np


class NeuronNetwork:
    def __init__(self, x, y):
        # x is input layers, and y is output layers
        self.x = x
        self.y = y 

        # returns the dimensions of y
        self.output = np.zeros(self.y.shape)

        # this will get a matrix with random numbers 
        self.W1 = np.random.rand(self.input.shape[1], 4)
        self.W2 = np.random.rand(4, 1)

    # sigmoid function
    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    # feedforward function
    # calculate the output
    def forward(self):
        layer = sigmoid(np.dot(self.x, self.W1))
        self.output = sigmoid(np.dot(layer, self.W1))


# next we will build a backward function and maybe train function
