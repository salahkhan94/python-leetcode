class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Rows and columns

        for i in range(len(board)):
            r = set()
            c = set()
            for j in range(len(board)):
                if (board[i][j] != '.'):
                    if(board[i][j] in r):
                        return False
                    else :
                        r.add(board[i][j])
                if (board[j][i] != '.'):
                    if(board[j][i] in c):
                        return False
                    else :
                        c.add(board[j][i])

        for i in range(0, 7, 3):
            r1 = set()
            r2 = set()
            r3 = set()
            for j in range(0, 3):
                for k in range(0, 3):
                    if (board[j][k + i] != '.'):
                        if (board[j][k + i] in r1):
                            return False
                        else :
                            r1.add(board[j][k + i])
                    
                    if (board[j + 3][k + i] != '.'):
                        if (board[j + 3][k + i] in r2):
                            return False
                        else :
                            r2.add(board[j + 3][k + i])

                    if (board[j + 6][k + i] != '.'):
                        if (board[j + 6][k + i] in r3):
                            return False
                        else :
                            r3.add(board[j + 6][k + i])
        
        return True


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]  # 3x3 sub-boxes

        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val == ".":
                    continue

                # Check row
                if val in rows[i]:
                    return False
                rows[i].add(val)

                # Check column
                if val in cols[j]:
                    return False
                cols[j].add(val)

                # Check 3x3 sub-box
                box_index = (i // 3) * 3 + (j // 3)
                if val in boxes[box_index]:
                    return False
                boxes[box_index].add(val)

        return True
