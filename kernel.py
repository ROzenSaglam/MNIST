import numpy as np

### Functions for you to fill in ###



def polynomial_kernel(X, Y, c, p):
    """
        Compute the polynomial kernel between two matrices X and Y::
            K(x, y) = (<x, y> + c)^p
        for each pair of rows x in X and y in Y.

        Args:
            X - (n, d) NumPy array (n datapoints each with d features)
            Y - (m, d) NumPy array (m datapoints each with d features)
            c - a coefficient to trade off high-order and low-order terms (scalar)
            p - the degree of the polynomial kernel

        Returns:
            kernel_matrix - (n, m) Numpy array containing the kernel matrix
    """
    # Compute dot product between each pair of rows in X and Y
    dot_products = np.dot(X, Y.T)
    
    # Compute kernel matrix using the polynomial kernel function
    kernel_matrix = (dot_products + c) ** p
    
    return kernel_matrix
    raise NotImplementedError



def rbf_kernel(X, Y, gamma):
    """
        Compute the Gaussian RBF kernel between two matrices X and Y::
            K(x, y) = exp(-gamma ||x-y||^2)
        for each pair of rows x in X and y in Y.

        Args:
            X - (n, d) NumPy array (n datapoints each with d features)
            Y - (m, d) NumPy array (m datapoints each with d features)
            gamma - the gamma parameter of gaussian function (scalar)

        Returns:
            kernel_matrix - (n, m) Numpy array containing the kernel matrix
    """
    X_norm = np.sum(X ** 2, axis=1, keepdims=True)
    Y_norm = np.sum(Y ** 2, axis=1, keepdims=True)
    norms = -2* X @ Y.T + X_norm + Y_norm
    kernel = np.exp(-gamma* norms)
    return kernel
    raise NotImplementedError
