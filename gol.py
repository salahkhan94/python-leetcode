class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        nextboard = [[0 for _ in range(n)] for _ in range(m)]

        for i in range(m):
            for j in range(n):
                liveneighbours = 0
                dirs = [-1, 0, 1]
                for dr in dirs:
                    for dc in dirs:
                        if (dr == 0 and dc == 0) : 
                            continue
                        nr = i + dr
                        nc = j + dc
                        if (nr >= 0 and nr < m and nc >=0 and nc < n and board[nr][nc] == 1):
                            liveneighbours += 1
                
                if board[i][j] == 1 : 
                    if liveneighbours < 2 or liveneighbours > 3:
                        nextboard[i][j] = 0
                    else : 
                        nextboard[i][j] = 1
                elif liveneighbours == 3:
                    nextboard[i][j] = 1
        
        board[:] = nextboard


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])

        new_board = [[0 for _ in range(n)] for _ in range(m)]

        for i in range(m):
            for j in range(n):
                liveneighbours = 0
                d = [-1, 0, 1]
                for k in d:
                    for l in d:
                        if k == 0 and l == 0:
                            continue
                        o = i + k
                        p = j + l
                        if (o >=0 and o < m and p >= 0 and p < n):
                            liveneighbours += board[o][p]
        
                if (liveneighbours < 2):
                    new_board[i][j] = 0
                if (liveneighbours > 1 and liveneighbours < 4 and board[i][j]):
                    new_board[i][j] = 1
                if (liveneighbours > 3):
                    new_board[i][j] = 0
                if (liveneighbours == 3 and board[i][j] == 0):
                    new_board[i][j] = 1
        
        board[:] = new_board