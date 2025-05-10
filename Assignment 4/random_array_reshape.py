# This program generates a random array of 16 elements, sorts it, and reshape it into a 4x4 matrix.

import numpy as np

# Generate a random array of 16 elements
arr = np.random.randint(1, 100, size=16)

print("Original Array:")
print(arr)

# Sort the array
sorted_arr = np.sort(arr)

# Reshape to 4x4 matrix
reshaped_matrix = sorted_arr.reshape(4, 4)

print("\nSorted & Reshaped 4x4 Matrix:")
print(reshaped_matrix)