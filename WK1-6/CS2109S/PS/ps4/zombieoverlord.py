import numpy as np

def feature_scaling(X):
    '''
    Mean normalized each feature column.

    Parameters
    ----------
    X (np.ndarray) : (m, n) numpy matrix representing feature matrix

    Returns
    -------
        A (m, n) numpy matrix where each column has been mean-normalized.
    '''
    colmean = np.mean(X, axis=0)
    colstd = np.std(X, axis=0)
    Xscaled = (X - colmean) / colstd
    
    return Xscaled


def create_polynomial_matrix(X, power=2):
    '''
    Create a polynomial matrix.

    Parameters
    ----------
    X: (m, 1) numpy matrix
        Input matrix containing m data points.

    power: int
        The maximum power to which X will be raised.

    Returns
    -------
    poly_matrix: (m, power) numpy matrix
        A matrix where each column contains X raised to the power from 0 to 'power'.
    '''
    powers = np.arange(1, power + 1)

    # Use np.tile to repeat X for each power and np.cumprod to calculate powers
    poly_matrix = np.tile(X, (1, power)) ** np.tile(powers, (X.shape[0], 1))

    return poly_matrix



def mean_squared_error(y_true, y_pred):
    '''
    Calculate mean squared error between y_pred and y_true.

    Parameters
    ----------
    y_true (np.ndarray) : (m, 1) numpy matrix consists of true values
    y_pred (np.ndarray) : (m, 1) numpy matrix consists of predictions
    
    Returns
    -------
    The mean squared error value.
    '''
  
    # Calculate the squared differences between y_true and y_pred
    squared_errors = np.square(y_pred - y_true)
    
    # Calculate the mean squared error
    mse = np.mean(squared_errors) / 2.0
    
    return mse


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


# Load the dataset
data = np.array([
    [60, 2, 3, 480000.0],
    [63, 2, 4, 450000.0],
    [65, 2, 1, 480000.0],
    [65, 2, 4, 360000.0],
    [66, 2, 5, 350000.0],
    [67, 2, 0, 400000.0],
    [67, 2, 1, 430000.0],
    [67, 2, 2, 450000.0],
    [67, 2, 3, 410000.0],
    [67, 2, 4, 390000.0],
    [67, 2, 5, 390000.0],
    [67, 2, 6, 390000.0],
    [68, 2, 1, 460000.0],
    [68, 2, 2, 400000.0],
    [68, 2, 3, 370000.0],
    [68, 2, 4, 360000.0],
    [68, 2, 6, 370000.0],
    [68, 2, 7, 400000.0],
    [68, 2, 8, 370000.0],
    [69, 2, 3, 420000.0],
    [70, 2, 3, 510000.0],
    [70, 2, 8, 370000.0],
    [73, 2, 5, 370000.0],
    [73, 2, 7, 380000.0],
    [83, 2, 1, 590000.0],
    [83, 3, 1, 650000.0],
    [83, 3, 2, 550000.0],
    [83, 3, 3, 550000.0],
    [83, 3, 4, 580000.0],
    [84, 3, 3, 560000.0],
    [86, 3, 2, 560000.0],
    [88, 3, 3, 510000.0],
    [89, 3, 1, 610000.0],
    [90, 3, 3, 500000.0],
    [90, 3, 4, 520000.0],
    [90, 3, 5, 490000.0],
    [91, 3, 0, 550000.0],
    [91, 3, 3, 620000.0],
    [92, 3, 1, 490000.0],
    [92, 3, 2, 590000.0],
    [92, 3, 3, 490000.0],
    [92, 3, 4, 510000.0],
    [92, 3, 5, 490000.0],
    [92, 3, 6, 490000.0],
    [92, 3, 7, 510000.0],
    [93, 3, 0, 490000.0],
    [93, 3, 1, 660000.0],
    [93, 3, 2, 540000.0],
    [93, 3, 3, 550000.0],
    [93, 3, 4, 490000.0],
    [93, 3, 5, 510000.0],
    [93, 3, 6, 490000.0],
    [93, 3, 7, 490000.0],
    [94, 3, 2, 590000.0],
    [94, 3, 3, 550000.0],
    [94, 3, 4, 490000.0],
    [94, 3, 5, 540000.0],
    [95, 3, 1, 700000.0],
    [95, 3, 2, 620000.0],
    [95, 3, 3, 530000.0],
    [95, 3, 4, 540000.0],
    [96, 3, 2, 600000.0],
    [96, 3, 7, 480000.0],
    [97, 3, 1, 660000.0],
    [97, 3, 2, 600000.0],
    [97, 3, 4, 440000.0],
    [98, 3, 5, 450000.0],
    [104, 3, 1, 720000.0],
    [105, 3, 0, 630000.0],
    [105, 3, 1, 670000.0],
    [105, 3, 2, 670000.0],
    [105, 4, 1, 610000.0],
    [108, 3, 1, 780000.0],
    [109, 3, 2, 700000.0],
    [110, 3, 3, 670000.0],
    [110, 3, 4, 660000.0],
    [111, 3, 3, 640000.0],
    [112, 3, 1, 700000.0],
    [112, 3, 2, 660000.0],
    [112, 3, 3, 670000.0],
    [112, 3, 4, 650000.0],
    [113, 3, 1, 640000.0],
    [113, 3, 2, 590000.0],
    [113, 3, 3, 600000.0],
    [113, 3, 4, 590000.0],
    [113, 3, 5, 590000.0],
    [115, 3, 1, 720000.0],
    [115, 3, 2, 700000.0],
    [119, 4, 3, 690000.0],
    [124, 3, 1, 770000.0]
])

# Extract the "schools" column as feature X and the target column as y
X = data[:, 2:3]  # Schools column
y = data[:, -1:]  # Asking price column

# Define different learning rates to test
learning_rates = [1e-5, 1e-4, 1e-3]

# Step 1: Transform "schools" column into a 3rd-degree polynomial matrix
power = 3
poly_matrix = create_polynomial_matrix(X, power)

# Step 2: Calculate the number of epochs for non-normalized data
print("Number of Epochs for Non-Normalized Data:")
for lr in learning_rates:
    _, _, num_epochs, _ = find_number_of_epochs(poly_matrix, y, lr, delta_loss=1e-5)
    print(f"Learning Rate {lr}: {num_epochs} epochs")

# Step 3: Calculate the number of epochs for mean-normalized data
scaled_poly_matrix = feature_scaling(poly_matrix)
print("\nNumber of Epochs for Mean-Normalized Data:")
for lr in learning_rates:
    _, _, num_epochs, _ = find_number_of_epochs(scaled_poly_matrix, y, lr, delta_loss=1e-5)
    print(f"Learning Rate {lr}: {num_epochs} epochs")
