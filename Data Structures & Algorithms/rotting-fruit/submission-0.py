"""
Multi-source BFS 
first collect indices where rotten oranges located, we also count # of fresh oranges. 
using queue we start from the sources - rotten oranges in queue
while queue 
    we pop the queue 
    and for every 4 directions 
        check if next move is in boundary of grid 
        check if next move is fresh orange 
            we mark the grid as rotten 
    increment minute

check if there are any remaining fresh oranges. 
"""
from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        fresh = 0
        queue = deque([])
        minutes = 0 

        for r in range(row):
            for c in range(col):
                if grid[r][c] == 2: 
                    queue.append((r, c))
                if grid[r][c] == 1: 
                    fresh += 1
        print(fresh, queue)
        while queue: 
            for _ in range(len(queue)):
                r, c = queue.popleft() 
                for dr, dc in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
                    nr, nc = r + dr, c + dc 
                    # check boundary and rotten 
                    if nr >= 0 and nc >= 0 and nr < row and nc < col and grid[nr][nc] == 1:
                        queue.append((nr, nc))
                        grid[nr][nc] = 2
                        fresh -= 1
            if queue:
                minutes += 1
        return minutes if fresh == 0 else -1

        