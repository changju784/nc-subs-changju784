"""
Key Points 
1. (0, n-1) and (m-1, 0) already face with two waters 
2. 
"""
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        row = len(heights)
        col = len(heights[0])
        pacific = set() 
        atlantic = set() 

        def dfs(r, c, visited, prev):
            if r < 0 or r >= row or c < 0 or c >= col or (r, c) in visited or heights[r][c] < prev:
                return None 
            visited.add((r, c))
            # recurse 4 directions 
            dfs(r+1, c, visited, heights[r][c])
            dfs(r-1, c, visited, heights[r][c])
            dfs(r, c+1, visited, heights[r][c])
            dfs(r, c-1, visited, heights[r][c])

        for r in range(row): 
            dfs(r, 0, pacific, heights[r][0]) # pacific
            dfs(r, col-1, atlantic, heights[r][col-1]) #atl
        for c in range(col):
            dfs(0, c, pacific, heights[0][c]) # pac
            dfs(row -1, c, atlantic, heights[row - 1][c]) # atl
        
        result = [] 
        for r, c in pacific:
            if (r, c) in atlantic:
                result.append([r, c])
        return result
