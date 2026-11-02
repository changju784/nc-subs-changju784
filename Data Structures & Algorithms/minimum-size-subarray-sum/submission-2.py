"""
input: integer array nums and target k 
output: minimum size of subarray that reaches target, if none 0 
constraints: 
len(num) > 0 
nums[i] > 0 

Brute Force O(N^2) O(1)
Generate all the subarray 
Check if current subarray matches the condition (> target)
    record the minimum length 

Sliding window O(N) O(1)
Right pointer keep moving right and adds nums[r] to curr_sum 
once we reached curr_sum >= target 
Decrement current sum by moving left pointer 
record the minimum window size 

[2,1,5,1,5,3] 
         R
     L
curr_sum = 11
while curr_sum - nums[l] >= target 
    curr_sum -= nums[l]
    l += 1
"""
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        curr_sum = 0 
        min_len = float('inf')

        for r in range(len(nums)): 
            curr_sum += nums[r]
            while curr_sum - nums[l] >= target: 
                curr_sum -= nums[l]
                l += 1
            if curr_sum >= target:
                min_len = min(min_len, r - l + 1) 

        
        return min_len if min_len != float('inf') else 0 




        