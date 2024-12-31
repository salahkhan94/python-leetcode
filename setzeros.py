class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        firstrowzero = False
        firstcolzero = False

        for i in range(len(matrix)):
            if(matrix[i][0] == 0):
                firstcolzero = True
        for i in range(len(matrix[0])):
            if(matrix[0][i] == 0):
                firstrowzero = True

        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if (matrix[i][j] == 0):
                    matrix[0][j] = 0
                    matrix[i][0] = 0
                            
        for i in range(1, len(matrix)):
            if matrix[i][0] == 0:
                for j in range(1, len(matrix[i])):
                    matrix[i][j] = 0
        
        for i in range(1, len(matrix[0])):
            if matrix[0][i] == 0:
                for j in range(1, len(matrix)):
                    matrix[j][i] = 0
        
        if firstrowzero :
            for i in range(len(matrix[0])):
                matrix[0][i] = 0
        
        if firstcolzero : 
            for i in range(len(matrix)):
                matrix[i][0] = 0
