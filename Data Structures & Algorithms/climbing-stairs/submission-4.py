"""
input: integer n -> 
output: integer, count of distinct ways to get from 0 to n by taking either 1 or 2 steps. 

constraints: 
0 < n

n = 5
[-, -, -, -, -]

DFS 
params - i (current step)
basecase - i > n: invalid. return 0 i == n: valid return 1
return - consider current step as 1 + recursion + recursion 

dfs(0) -> 3 0  n = 3
      dfs(1) -> 2, dfs(2) -> 1
dfs(1) 1 
      dfs(2) -> 1, dfs(3) -> 1
dfs(2) 2
      dfs(3) -> 1, dfs(4) -> 0
dfs(3) 3 -> 1

TC: O(2**n)
SC: O(n)

DP memoization 
we can cache how many remaining steps are there at each step 
[3, 2, 1]
"""
class Solution:
    def climbStairs(self, n: int) -> int:
        cache = [0] * n
        def dfs(i: int):
            if i > n: 
                return 0 
            if i == n: 
                return 1 
            if cache[i] > 0: 
                return cache[i]

            cache[i] = dfs(i+1) + dfs(i+2)
            return cache[i]
            
        return dfs(0)
