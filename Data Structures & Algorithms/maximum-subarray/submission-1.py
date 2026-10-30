class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        Key points 
        1. Contiguous 

        Brute Force 
        For each element, search for maximum subarray containing current element
        Cache sum of contiguous subarrays 

        Dynamic programming 
        in each element we have two choices, whether to include current sum or not 

        """
        cache = [0] * len(nums)
        cache[0] = nums[0]
        for i in range(1, len(nums)): 
            cache[i] = max(cache[i-1] + nums[i], nums[i])

        return max(cache)

            
