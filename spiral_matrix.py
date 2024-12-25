class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        spiral = []

        for i in range(len(matrix)):
             l = len(matrix)
             for j in range(l):
                if i%2 == 0 :
                    spiral.append(matrix[i][j])
                else :
                    spiral.append(matrix[j][i])
                    