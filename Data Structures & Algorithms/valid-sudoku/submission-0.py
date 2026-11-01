"""
for each row, col, and 3x3 sqaures
find if there are duplicates

iterate row by row 

0,0 0,3 0,6
3,0 3,3, 3,6
6,0 6,3, 6,6 
"""
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = len(board)
        col = len(board[0])
        
        for r in range(row):
            row_set = set() 
            for c in range(col):
                if board[r][c] == ".":
                    continue
                if board[r][c] in row_set:
                    return False
                row_set.add(board[r][c])
        
        for c in range(col):
            col_set = set() 
            for r in range(row):
                if board[r][c] == ".":
                    continue
                if board[r][c] in col_set: 
                    return False 
                col_set.add(board[r][c])

        for square in range(9):
            seen = set()
            for i in range(3):
                for j in range(3):
                    r = (square//3) * 3 + i
                    c = (square % 3) * 3 + j
                    if board[r][c] == ".":
                        continue
                    if board[r][c] in seen:
                        return False
                    seen.add(board[r][c])
        return True 
        

