# This program creates a NumPy array of random values with user_defined shape (a, b) and calculates the average.

import numpy as np

# Get user input for shape
a = int(input("Enter number of rows (a): "))
b = int(input("Enter number of columns (b): "))

# Create random array of shape (a, b)
random_array = np.random.rand(a, b)

# Display the array
print("Random Array:")
print(random_array)

# Compute and display average
average = np.mean(random_array)
print("Average of all elements:", average)