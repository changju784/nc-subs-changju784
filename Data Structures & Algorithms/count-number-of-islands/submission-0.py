class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        '1' - land '0' - water 
        island - v | h connected lands '
        return number of islands 

        DFS 
        starting from the root check top bottom left right of the grid 
        once it's connected mark off visited 
        """
        
        def DFS(r, c): 
            if r >= row or c >= col or r < 0 or c < 0: # out of grid
                return 
            if grid[r][c] == "0" or (r, c) in visited: # if water 
                return 
            
            visited.add((r, c))
            DFS(r-1, c) # up 
            DFS(r+1, c) # down 
            DFS(r, c-1) # left
            DFS(r, c+1) # right

        row = len(grid)
        col = len(grid[0])
        num_of_islands = 0 
        visited = set() 

        for r in range(row):
            for c in range(col): 
                if grid[r][c] == '1' and (r,c) not in visited: 
                    DFS(r, c)
                    num_of_islands += 1

        return num_of_islands