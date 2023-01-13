import numpy as np

def sigmoid(x):
    return 1 / (1+np.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)

training_inputs = np.array([[0,0,1],[1,1,1],[1,0,1],[0,1,1]])

training_outputs = np.array([[0,1,1,0]]).T
np.random.seed(1)

synaptic_weights = 2* np.random.random((3,1))-1

print('Random starting synaptic weigts: ')
print(synaptic_weights)

for interaction in range(100000):
    input_layer = training_inputs
    outputs = sigmoid(np.dot(input_layer,synaptic_weights))

    error = training_outputs - outputs
    moderator = error * sigmoid_derivative(outputs)
    synaptic_weights += np.dot(input_layer.T,moderator)

print('Final Synaptic weights: ')
print(synaptic_weights)
print('Final training Outputs: ')
print(outputs)