import numpy as np
# Define the blocks
block1 = np.array([[1, 1], 
                   [1, 1]])

block2 = np.array([[2, 2, 2], 
                   [2, 2, 2], 
                   [2, 2, 2]])

block3 = np.array([[3]])

# Create the block diagonal matrix
# Using np.block is the most flexible way in modern NumPy
from scipy.linalg import block_diag # Standard library for this task

block_matrix = block_diag(block1, block2, block3)

print("Block Diagonal Matrix:")
print(block_matrix)