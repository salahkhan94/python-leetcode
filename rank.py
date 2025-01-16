import numpy as np


matrix = np.array([[3, 4, 5, 7],
                   [2, 3, 8, 4],
                   [3, 7, 3, 5],
                   [5, 5, 7, 1]])

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

matrix4 = np.array([[0, 0, 0],
                    [1/np.sqrt(2), 0, -1/np.sqrt(2)],
                    [0, 1, 0]])

rank4 = np.linalg.matrix_rank(matrix4)
print(rank4)
U, S, Vt = np.linalg.svd(matrix4)
print(S)
matrix5 = np.array([[2, 0, 0],
                    [0, 1, 0],
                    [0, 0, 0]])
rank5 = np.linalg.matrix_rank(matrix5)
print(rank5)
U, S, Vt = np.linalg.svd(matrix5)
print(S)