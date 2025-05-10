# This program creates a 5x5 matrix where each row contains values from 0 to 4.

import numpy as np

# Creat a 5x5 matrix using broadcasting
matrix = np.tile(np.arange(5), (5, 1))

# Display the matrix
print("5x5 Matrix with each row from 0 to 4:")
print(matrix)