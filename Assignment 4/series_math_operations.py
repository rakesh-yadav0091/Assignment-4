# This program creates two Pandas Series and performs element-wise addition, subtraction, multiplication, and division.

import pandas as pd

# Create two sample series
series1 = pd.Series([10, 20, 30, 40, 50])
series2 = pd.Series([1, 2, 3, 4, 5])

# Perform operations
print("Series 1:")
print(series1)

print("\nSeries 2:")
print(series2)

print("\nAddition:")
print(series1 + series2)

print("\nSubtraction:")
print(series1 - series2)

print("\nMultiplication:")
print(series1 * series2)

print("\nDivision:")
print(series1 / series2)