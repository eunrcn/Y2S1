import numpy as np

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
