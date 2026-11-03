import numpy as np


# Step activation function
def activation(x):
    if x >= 0:
        return 1
    return 0


# Training data for AND gate
X = np.array([
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
])

y = np.array([0, 0, 0, 1])


# Initialize weights and bias
weights = np.zeros(2)
bias = 0

learning_rate = 0.1
epochs = 10


# Training
for epoch in range(epochs):

    for i in range(len(X)):

        # Calculate weighted sum
        z = np.dot(X[i], weights) + bias

        # Prediction
        prediction = activation(z)

        # Calculate error
        error = y[i] - prediction

        # Update weights
        weights = weights + learning_rate * error * X[i]

        # Update bias
        bias = bias + learning_rate * error


print("Training completed")
print("Weights:", weights)
print("Bias:", bias)


# Testing
print("\nPredictions:")

for x in X:
    z = np.dot(x, weights) + bias
    prediction = activation(z)

    print(x, "->", prediction)