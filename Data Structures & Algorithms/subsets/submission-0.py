"""
Backtracking

sort the nums before recursion so that we prevent duplicates
for every path, we need to check if current path can be included in answer 
basecase- if current path of length is over len(nums)
if current path already exists 
"""
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        nums.sort() 
        ans = [] 

        def backtrack(i, path):
            ans.append(path[:])
            for j in range(i, len(nums)):
                path.append(nums[j])
                backtrack(j+1, path)
                path.pop()
            return 
        backtrack(0,[])
        return ans