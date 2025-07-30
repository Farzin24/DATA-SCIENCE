# matrix_user_input.py

import numpy as np

# Function to take user input for a 3x3 matrix
def get_matrix(name):
    print(f"\nEnter values for Matrix {name} (3x3):")
    matrix = []
    for i in range(3):
        row = input(f"Enter row {i+1} (3 numbers separated by space): ").split()
        matrix.append([int(x) for x in row])
    return np.array(matrix)

# Get matrices from user
A = get_matrix("A")
B = get_matrix("B")

scalar = int(input("\nEnter a scalar value for scalar multiplication: "))

# Display entered matrices
print("\nMatrix A:\n", A)
print("Matrix B:\n", B)

# Perform operations
print("\n(a) A + B:\n", A + B)
print("\n(b) A - B:\n", A - B)
print("\n(c) A * B (matrix multiplication):\n", A @ B)
print("\n(d) Scalar * A:\n", scalar * A)
print("\n(e) Transpose of A:\n", A.T)

