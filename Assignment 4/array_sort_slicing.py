# This program takes an array input from the user, sorts it, and slices it (first 3 and last 3 elements).

import numpy as np

# Get user input and convert to NumPy array
user_input = input("Enter numbers separated by spaces: ")
arr = np.array(list(map(int, user_input.strip().split())))

# Sort the array
sorted_arr = np.sort(arr)

# Display full, sliced arrays
print("Sorted Array:", sorted_arr)
print("First 3 elements:", sorted_arr[:3])
print("Last 3  elements:", sorted_arr[-3:])