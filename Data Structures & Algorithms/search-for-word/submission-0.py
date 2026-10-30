class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # Backtracking DFS 
        def DFS(r, c, depth): 
            if r < 0 or r >= row or c < 0 or c >= col: 
                return False 
            if board[r][c] != word[depth]: 
                return False 
            if (r, c) in visited: 
                return False
            if depth == len(word)-1:
                return True
            
            visited.add((r, c))
            if DFS(r+1, c, depth+1) or DFS(r-1, c, depth+1) or DFS(r, c+1, depth+1) or DFS(r, c-1, depth+1): 
                return True 
            visited.remove((r, c))
            return False


        row = len(board)
        col = len(board[0])
        visited = set()
        for r in range(row): 
            for c in range(col): 
                if board[r][c] == word[0]: 
                    if DFS(r, c, 0): 
                        return True 
        return False  
