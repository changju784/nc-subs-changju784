"""
Brute Force + DFS 
Get indices of zeros 
Iterate through the zero indices 
    Run DFS to compute the area 
DFS
basecase - when out of boundary, if it's not 1 
"""
class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        zeros = set() 
        # get all zero indices 
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 0: 
                    zeros.add((r, c))
        if len(zeros) == 0: 
            return row * col 
        
        def dfs(r, c): 
            if r < 0 or r >= row or c < 0 or c >= col or grid[r][c] == 0 or (r, c) in visited: 
                return 0 
            visited.add((r, c))
            area = 1 + dfs(r+1, c) + dfs(r-1, c) + dfs(r, c+1) + dfs(r, c-1)
            return area 
        
        max_area = 0 
        for r, c in zeros: 
            grid[r][c] = 2 
            visited = set() 
            area = dfs(r, c)
            max_area = max(max_area, area)
            grid[r][c] = 0 
        return max_area

