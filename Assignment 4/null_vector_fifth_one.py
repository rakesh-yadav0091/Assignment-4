# This program creates a NumPy null vector of size 10 with the 5th element set to 1.

import numpy as np

# Create a null vector (all zeros)
vector = np.zeros(10)

#set the 5th element (index 4)to 1
vector[4] = 1

# Display the result
print("Null vector with the 5th value as 1:")
print(vector)