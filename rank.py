import numpy as np

# Example matrix
matrix = np.array([[3, 4, 5, 7],
                   [2, 3, 8, 4],
                   [3, 7, 3, 5],
                   [5, 5, 7, 1]])

# Calculate the rank
rank = np.linalg.matrix_rank(matrix)

print(f"The rank of the matrix is: {rank}")


matrix2 = np.array([[0, -0.8, 1],
                    [1, 0, 1],
                    [2.2, 0.9, 1],
                    [2.9, 2.1, 1]])

U, S, Vt = np.linalg.svd(matrix2)

print(Vt.T)


matrix3 = np.array([[-2, 0, 0],
                    [0, 0, 0],
                    [0, 1, 0]])

U, S, Vt = np.linalg.svd(matrix3)
print(S)