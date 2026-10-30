"""
BackTracking 
Each step we can either add myself, or move on to other number
once we reached curr_sum > target: return 
if curr_sum == target: add it to set 
recurse to include myself, or move to next one. 
prune curr_sum - curr_num

!! important 
when designing dfs or recursion make sure to 
1. set basecase. when recursion reaches the end 
2. what to return. what do we return in deeper callstack to upper. 
3. params. 
"""
class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        def dfs(i, curr_sum, curr_nums):
            if curr_sum > target: 
                return None 
            if curr_sum == target: 
                result.append(curr_nums)
                return None 
            if i == len(nums):
                return None 
            
            dfs(i, curr_sum + nums[i], curr_nums + [nums[i]]) # recurse myself
            dfs(i+1, curr_sum, curr_nums) # not doing anything move on 
            
        dfs(0, 0, [])
        return result 

            



        