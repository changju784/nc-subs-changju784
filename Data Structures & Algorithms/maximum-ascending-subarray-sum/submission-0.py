"""
prefix sum O(N) O(1)
while iterating through the list compare with prev < curr 
if so accumulate to prefix sum 
if not record the running sum and reset it 

[10,20,30,5,10,50]
                ^
curr = 65 
max = 60
"""
class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        if len(nums) == 1: 
            return nums[0]

        max_sum = 0 
        curr_sum = nums[0] 
        for i in range(1, len(nums)):
            if nums[i-1] < nums[i]: # strictly increasing
                curr_sum += nums[i]
            else: 
                max_sum = max(max_sum, curr_sum)
                curr_sum = nums[i]
        
        return max(max_sum, curr_sum)


        