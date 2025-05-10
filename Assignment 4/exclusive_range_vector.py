# This program creates a NumPy vector with values ranging from 0 to 1 (excluded) using 10 eually spaced points.

import numpy as np

# Create 10 values between 0 and 1, excluding 1
vector = np.linspace(0, 1, 10, endpoint=False)

# Display the vector
print("Vector with values from 0 to 1 (excluded):")
print(vector)