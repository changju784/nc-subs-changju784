"""
DFS in-place O(m*n) O(1)
basecase - when reached the end return 0 
mark current cell visited 


"""
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != 1: 
                return 0
            
            grid[r][c] += 1

            return 1 + dfs(r+1, c) + dfs(r-1, c) + dfs(r, c+1) + dfs(r, c-1)

        rows = len(grid)
        cols = len(grid[0])
        area, max_area = 0, 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1: 
                    max_area = max(max_area, dfs(r, c))
        return max_area

        