"""
input: integer list, target int
output: all combinations sum to target 

constratins: 
may contain duplicate 
any element at most once 

Backtracking 
params - index, path
basecase - when current sum of comb exceeds target, return 
         - when current index is in visited, return 
         - when current sum == target, append to result, return 
         add current index to visited 
         loop through candidates 
            recurse next possibilities
         - prune visited 

[9,2,2,4,6,1,5]
 ^ 
visited = {0} 
path = [9]

TC: O(n * 2^n)
SC: O(n)
"""
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()

        def backtrack(i, path, path_sum): 
            if path_sum == target: 
                result.append(path[:])
                return 

            if path_sum > target: 
                return 
            
            for j in range(i, len(candidates)):
                if j > i and candidates[j-1] == candidates[j]: continue # prevent dup
                if path_sum + candidates[j] > target: break 

                path.append(candidates[j])
                backtrack(j+1, path, path_sum + candidates[j])
                path.pop() 

        
        backtrack(0, [], 0)
        return result

"""
[9,2,2,4,6,1,5]

 dfs(9) [9] {0}
 dfs(9) [9] {0}  dfs(2)
"""
        