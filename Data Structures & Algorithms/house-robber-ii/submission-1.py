"""
input - nums integer list that contains money in ith houses. 
ouput - maximum amount based on condition 

1. in each step we have two choices, rob -> move to i+2, skip -> move to i+1 

recursion 
params - i, curr_sum 
basecase - when i > len(nums) return 0
"""
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: 
            return nums[0]
        
        dp = [[-1] * 2 for _ in range(len(nums))]

        def dfs(i, robbed_first):
            if i >= len(nums):
                return 0
            if i == len(nums)-1 and robbed_first: 
                return 0
            if dp[i][robbed_first] > -1: 
                return dp[i][robbed_first]
            dp[i][robbed_first] = max(dfs(i+1, robbed_first), nums[i] + dfs(i+2, robbed_first))
            return dp[i][robbed_first]
        max_money = max(dfs(0, True), dfs(1, False))
        return max_money


        