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