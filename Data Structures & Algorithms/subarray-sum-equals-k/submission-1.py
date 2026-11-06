"""
Brute force O(N^2) O(1)
Generate all subarrays 
    once the subarray sum reaches k count up 

[2, -1, 1, 0, 2]
     
[0,  2, 1, 2, 2]
[2,  1, 2, 2, 4]

Prefix Sum + Hashmap 
key - prefixsum, val - freq 
Iterate through num
    update prefix sum 
    record it in hashmap 
    update curr sum 
    if curr_sum - k exists in hashmap
        counter up result by hashmap[curr_sum - k] 
return result 
"""
from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        result = 0 
        prefix_sum_map = defaultdict(int) # key - prefix sum, val - freq 
        curr_sum = 0

        for i in range(len(nums)):
            # update prefix sum
            prefix_sum_map[curr_sum] += 1
            
            # update curr sum 
            curr_sum += nums[i]

            # check if target exists in map 
            if curr_sum - k in prefix_sum_map:
                result += prefix_sum_map[curr_sum - k]
        return result
            

            




        