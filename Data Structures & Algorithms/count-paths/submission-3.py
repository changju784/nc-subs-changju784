"""
DFS Time - O(2^(m+n)) Space - O(m+n)
base case - when it reaches the end (target) return 1 
when it reaches out of boundary return 0 
two choices in every call stack, either move right or down 

2D DP 
each cell contains possible path from that cell. 

"""
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[-1] * n for _ in range(m)]
        
        def DFS(r, c):
            if r == m-1 and c == n-1: 
                return 1 
            if r >= m or c >= n: 
                return 0 
            if dp[r][c] != -1: 
                return dp[r][c]
            dp[r][c] = DFS(r, c+1) + DFS(r+1, c)
            return dp[r][c] 
            
        return DFS(0, 0)