import numpy as np

def find_number_of_epochs(X, y, lr, delta_loss):
    '''
    Do gradient descent until convergence and return number of epochs
    required.

    Parameters
    ----------
    X (np.ndarray) : (m, n) numpy matrix representing feature matrix
    y (np.ndarray) : (m, 1) numpy matrix representing target values
    lr (float) : Learning rate
    delta_loss (float) : Termination criterion
    
    Returns
    -------
        bias (float):
            The bias constant
        weights (np.ndarray):
            A (n, 1) numpy matrix that specifies the weight constants.
        num_of_epochs (int):
            Number of epochs to reach convergence.
        current_loss (float):
            The loss value obtained after convergence.
    '''
    # Initialize variables
    bias = 0
    weights = np.full((X.shape[1], 1), 0).astype(float)
    num_of_epochs = 0
    previous_loss = float('inf')  # Initialize with a large value
    current_loss = mean_squared_error(y, X @ weights + bias)

    # Run gradient descent until convergence
    while abs(previous_loss - current_loss) >= delta_loss:
        # Update previous loss
        previous_loss = current_loss
        
        # Calculate gradients for bias and weights
        bias_gradient = (1 / X.shape[0]) * np.sum(X @ weights + bias - y)
        weights_gradient = (1 / X.shape[0]) * (X.T @ (X @ weights + bias - y))

        # Update bias and weights using the gradients and learning rate
        bias -= lr * bias_gradient
        weights -= lr * weights_gradient.reshape(-1, 1)

        # Calculate current loss
        current_loss = mean_squared_error(y, X @ weights + bias)

        # Increment the number of epochs
        num_of_epochs += 1

    return bias, weights, num_of_epochs, current_loss
