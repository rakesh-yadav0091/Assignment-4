# This program performs multiple DataFrame operations on employee data using pandas.

import pandas as pd

# Create DataFrame
data = {
    'Emp_ID': [101, 102, 103, 104, 105],
    'Name': ['Rakesh', 'Ram', 'Shyam', 'Sita', 'Gita'],
    'Age': [21, 24, 22, 19, 20],
    'Department': ['IT', 'Finance', 'HR', 'IT', 'HR'],
    'Salary': [50000, 40000, 45000, 48500, 42000]
}

df = pd.DataFrame(data)

# Display original DataFrame
print("Employee DataFrame:\n", df)

# a. Filter employee whose salary is more than 45000
print("\nEmployees with Salary > 45000:")
print(df[df['Salary'] > 45000])

# b. Average salary of all employees
avg_salary = df['Salary'].mean()
print("\nAverage Salary:", avg_salary)

# c. Add a new column for bonus (10% of salary)
df['Bonus'] = df['Salary'] * 0.10
print("\nDataFrame with Bonus Column:")
print(df)