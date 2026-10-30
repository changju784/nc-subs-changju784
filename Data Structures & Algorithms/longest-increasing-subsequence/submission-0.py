class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # This is not finding global max or min 
        # Dynamic programming 
        # From each element check what would be the LIS
        
        dp = [1] * len(nums)

        for i in range(len(nums)): 
            for j in range(i): 
                if nums[j] < nums[i]: 
                    # update dp
                    dp[i] = max(dp[i], dp[j]+1)
        return max(dp)
        
                     
