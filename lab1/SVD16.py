import numpy as np

n = int(input("Enter size of square matrix: "))
A = [list(map(float, input().split())) for _ in range(n)]
A = np.array(A)

U, S, VT = np.linalg.svd(A)
S_matrix = np.zeros((n, n))
np.fill_diagonal(S_matrix, S)
A_reconstructed = U @ S_matrix @ VT

print("Original Matrix:\n", A)
print("Reconstructed Matrix:\n", np.round(A_reconstructed, 2))
