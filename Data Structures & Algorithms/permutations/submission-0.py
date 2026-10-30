"""
input: integers list 
output: list of all permutations 

all possibilities of perms -> n! 
each step we can choose numbers have not been used in previous steps 

recursion - backtracking 
params - current number 
basecase - when we reached the path that has length of len(nums)
         - append this to result 
         - within recursion traverse the entire nums 
         - remove the path that has been visited 
TC: O(N!)
SC: O(N)
"""
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0: 
            return [[]]
        result = [] 
        pick = [False] * len(nums)

        def backtrack(path, pick):
            # basecase - store result 
            if len(path) == len(nums):
                result.append(path[:])
                return 
            
            # traverse nums and select which perm to be picked
            for i in range(len(nums)): 
                if not pick[i]: 
                    pick[i] = True
                    path.append(nums[i]) 
                    backtrack(path, pick)
                    # remove the visited path 
                    path.pop() 
                    pick[i] = False 
        
        backtrack([], pick)
        return result

            

        