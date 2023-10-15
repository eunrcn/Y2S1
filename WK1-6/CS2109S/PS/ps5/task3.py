import matplotlib.pyplot as plt
from time import time
import numpy as np

X_sample = np.random.rand(100, 2)  # Initialize X_sample with random data (100 samples, 2 features)
y_sample = np.random.randint(0, 2, size=100)  # Initialize y_sample with random binary labels (0 or 1)
# Initialize your X_sample and y_sample
# Define the number of iterations
num_iterations = 250

batch_times = []
batch_costs = []
stochastic_times = []

def cost_function(X: np.ndarray, y: np.ndarray, weight_vector: np.ndarray):
    # Machine epsilon for numpy float64 type
    eps = np.finfo(np.float64).eps

    m = X.shape[0]  # Number of samples
    z = np.dot(X, weight_vector)  # Compute the linear combination

    # Calculate the logistic sigmoid function
    sigmoid = 1 / (1 + np.exp(-z))

    # Calculate the cost using the cross-entropy formula
    cost = -np.mean(y * np.log(sigmoid + eps) + (1 - y) * np.log(1 - sigmoid + eps))

    return cost

def weight_update_stochastic(X, y, alpha, weight_vector):
    # Calculate the predicted value
    z = np.dot(X, weight_vector)
    sigmoid = 1 / (1 + np.exp(-z))

    # Calculate the gradient for a single data point
    gradient = X * (y - sigmoid)

    # Update the weight vector
    updated_weight = weight_vector + alpha * gradient

    return updated_weight

def logistic_regression_stochastic_gradient_descent(X_train, y_train, max_num_iterations=250, threshold=0.05, alpha=1e-5):
    m, n = X_train.shape  # Number of samples and features
    weight_vector = np.zeros(n)  # Initialize weight vector to zeros
    num_iterations = 0  # Initialize the iteration counter

    # Initialize the error to the cost on the initial weight vector
    initial_cost = cost_function(X_train, y_train, weight_vector)
    error = initial_cost

    while num_iterations < max_num_iterations:
        # Randomly select a single data point
        random_index = np.random.randint(0, m)
        X_point = X_train[random_index]
        y_point = y_train[random_index]

        # Perform a stochastic weight update
        weight_vector = weight_update_stochastic(X_point, y_point, alpha, weight_vector)

        # Calculate the cost (cross-entropy error)
        cost = cost_function(X_train, y_train, weight_vector)

        # Check for early termination based on the threshold
        if cost <= threshold:
            break

        # Update the error to the current cost
        error = cost

        num_iterations += 1

    return weight_vector


def weight_update(X: np.ndarray, y: np.ndarray, alpha: np.float64, weight_vector: np.ndarray):
    m = X.shape[0]  # Number of samples
    z = np.dot(X, weight_vector)  # Compute the linear combination

    # Calculate the logistic sigmoid function
    sigmoid = 1 / (1 + np.exp(-z))

    # Calculate the gradient of the cost with respect to the weight parameters
    gradient = np.dot(X.T, sigmoid - y) / m

    # Update the weight vector using gradient descent
    updated_weight_vector = weight_vector - alpha * gradient

    return updated_weight_vector


stochastic_costs = []
def logistic_regression_batch_gradient_descent(X_train, y_train, max_num_epochs=250, threshold=0.05, alpha=1e-5):
    m, n = X_train.shape  # Number of samples and features
    weight_vector = np.zeros(n)  # Initialize weight vector to zeros
    num_update_rounds = 0  # Initialize the update counter

    while num_update_rounds < max_num_epochs:
        # Calculate the cost
        cost = cost_function(X_train, y_train, weight_vector)
        
        if cost <= threshold:
            break  # Terminate if cost is below threshold
        
        # Update the weights
        weight_vector = weight_update(X_train, y_train, alpha, weight_vector)
        
        num_update_rounds += 1

    return weight_vector


for i in range(50, num_iterations + 1, 50):
    # Measure runtime for batch gradient descent
    start = time()
    weight_vector = logistic_regression_batch_gradient_descent(X_sample, y_sample, i, 0, 1e-5)
    stop = time()
    batch_times.append(stop - start)
    batch_costs.append(cost_function(X_sample, y_sample, weight_vector))

for i in range(50, num_iterations + 1, 50):
    # Measure runtime for stochastic gradient descent
    start = time()
    weight_vector = logistic_regression_stochastic_gradient_descent(X_sample, y_sample, i, 0, 1e-5)
    stop = time()
    stochastic_times.append(stop - start)
    stochastic_costs.append(cost_function(X_sample, y_sample, weight_vector))

# Plot cross-entropy loss against the number of update rounds
plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
plt.plot(range(50, num_iterations + 1, 50), batch_costs, 'g^', label="Batch Gradient Descent")
plt.plot(range(50, num_iterations + 1, 50), stochastic_costs, 'bs', label="Stochastic Gradient Descent")
plt.xlabel('Number of Update Rounds')
plt.ylabel('Cross Entropy Loss')
plt.title('Cross Entropy Loss vs Number of Update Rounds')
plt.legend()

# Plot cross-entropy loss against runtime
plt.subplot(1, 2, 2)
plt.plot(batch_times, batch_costs, 'g^', label="Batch Gradient Descent")
plt.plot(stochastic_times, stochastic_costs, 'bs', label="Stochastic Gradient Descent")
plt.xlabel('Runtime (sec)')
plt.ylabel('Cross Entropy Loss')
plt.title('Cross Entropy Loss vs Runtime (sec)')
plt.legend()

plt.tight_layout()
plt.show()