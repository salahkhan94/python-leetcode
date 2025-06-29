class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        spiral = []
        m = len(matrix)
        n = len(matrix[0])

        left = 0
        right = n - 1
        top = 0
        bottom = m - 1

        while top <= bottom and left <= right:
            
            for col in range(left, right + 1):
                spiral.append(matrix[top][col])
            top += 1

            for row in range(top, bottom + 1):
                spiral.append(matrix[row][right])
            right -= 1

            if top <= bottom:
                for col in range(right, left - 1, -1):
                    spiral.append(matrix[bottom][col])
                bottom -= 1

            if left <= right:
                for row in range(bottom, top - 1, -1):
                    spiral.append(matrix[row][left])
                left += 1

        return spiral


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        spiral = []
        m = len(matrix)
        n = len(matrix[0])

        top = 0
        bottom = m-1
        left = 0
        right = n-1

        while (top <= bottom and left <= right) : 
            for i in range (left, right + 1):
                spiral.append(matrix[top][i])
            top += 1

            for i in range(top, bottom + 1):
                spiral.append(matrix[i][right])
            right -= 1

            if top <= bottom and left <= right :
                for i in range(right, left - 1, -1):
                    spiral.append(matrix[bottom][i])
            bottom -= 1

            if top <= bottom and left <= right :
                for i in range(bottom, top - 1, -1):
                    spiral.append(matrix[i][left])
            left += 1
        
        return spiral