import numpy as np

def get_dominant_eigenvalue_and_eigenvector(data, num_steps):
    """
    data: np.ndarray – symmetric diagonalizable real-valued matrix
    num_steps: int – number of power method steps

    Returns:
    eigenvalue: float – dominant eigenvalue estimation after `num_steps` steps
    eigenvector: np.ndarray – corresponding eigenvector estimation
    """
    ### YOUR CODE HERE
    x = np.random.rand(len(data)) 
    x /= np.linalg.norm(x)
    for i in range(num_steps):
        x_new = data @ x 
        x_new = x_new / np.linalg.norm(x_new)
        x = x_new 

    eigenvalue = float((x.T @ data @ x) / (x.T @ x))

    return eigenvalue, x  