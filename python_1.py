import numpy as np
arr = np.array([1,2,3,4])
print(arr)

zeros = np.zeros((3,3))
print(zeros)

arr1 = np.array([10,20,30,40,50,60,70,80])
print(arr1)
print(arr1[2])
print(arr1[:3])

reshaped = arr1.reshape(2,4)
print(reshaped)

a= np.arange(1, 6)
b= np.arange(6, 11)
print(b)

print(a)

print(a+b)
print(a-b)
print(a*b)
print(a/b)

matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("original matrix is:",matrix)

transpose = matrix.T
print("transpose is :",transpose)

matrix2 = np.array([[9, 8, 7], [6, 5, 4], [3, 2, 1]])
print("2nd original matrix is",matrix2)
print("addition is",matrix + matrix2)
print("substraction is",matrix - matrix2)


import numpy as np

# Create a 4x4 matrix with random integers
matrix = np.random.randint(1, 100, size=(4, 4))

# Calculate sums
row_sums = np.sum(matrix, axis=1) # axis=1 is for rows
col_sums = np.sum(matrix, axis=0) # axis=0 is for columns

print("Matrix:\n", matrix)
print("Row Sums:", row_sums)
print("Column Sums:", col_sums)

import numpy as np

# 1. Create an example array
original_array = np.array([10, 20, 30, 40, 50])

# 2. Calculate min and max values
x_min = original_array.min()
x_max = original_array.max()

# 3. Apply the formula
normalized_array = (original_array - x_min) / (x_max - x_min)

print("Original Array:", original_array)
print("Normalized Array:", normalized_array)



matrix3 = np.random.randint(1, 100, size=(4, 4))
x_min = matrix3.min()
x_max = matrix3.max()
print(x_min)
print(x_max)
