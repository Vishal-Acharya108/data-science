import numpy as np

# Define a 2x2 matrix
A = np.array([[4, 7], 
              [2, 6]])

# 1. Compute the Determinant
det_A = np.linalg.det(A)

# 2. Compute the Inverse
# Note: A matrix must have a non-zero determinant to be invertible
if det_A != 0:
    inv_A = np.linalg.inv(A)
else:
    inv_A = "Matrix is singular and cannot be inverted"

print(f"Matrix A:\n{A}")
print(f"Determinant: {det_A}")
print(f"Inverse:\n{inv_A}")