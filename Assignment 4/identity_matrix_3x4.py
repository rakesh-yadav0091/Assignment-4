# This program creates a 3x4 matrix and checks if it's an identity matrix.(Identity matrix must be suare)

import numpy as np

# Create a 3x4 matrix
matrix = np.identity(3)

# Pad to make it 3x4
matrix_3x4 = np.pad(matrix, ((0, 0), (0, 1)), mode='constant', constant_values=0)

print("3x4 Matrix:")
print(matrix_3x4)

# Check identity property (only valid if suare)
if matrix_3x4.shape[0] == matrix_3x4.shape[1] and np.array_eual(matrix_3x4, np.identity(3)):
    print("It is an identity matrix.")
else:
    print("It is NOT an identity matrix because it's not square.")