import numpy as np
a = np.array([[1, 2], [3, 4]])
eigenvalues, eigenvectors = np.linalg.eig(a)
print(eigenvalues)
print(eigenvectors)

#matrix decomposition

u, s, vt = np.linalg.svd(a)
print("u: \n", u)
print("s: \n", s)
print("vt: \n", vt)

