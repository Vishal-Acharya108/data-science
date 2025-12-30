import numpy as np
# Define three matrices
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
C = np.array([[9, 1], [2, 3]])

# Verify Associative Property
lhs_assoc = (A @ B) @ C
rhs_assoc = A @ (B @ C)
assoc_check = np.allclose(lhs_assoc, rhs_assoc)

# Verify Distributive Property
lhs_dist = A @ (B + C)
rhs_dist = (A @ B) + (A @ C)
dist_check = np.allclose(lhs_dist, rhs_dist)

print(f"Associative Property holds: {assoc_check}")
print(f"Distributive Property holds: {dist_check}")
