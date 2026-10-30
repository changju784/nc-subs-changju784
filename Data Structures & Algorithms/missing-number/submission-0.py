"""
input: nums length of n 
output: missing number from [0, n] inclusive from the list. 

1. there's always going to be missing number. 
2. nums not sorted 

sum of the nums should be (n * (n+1)) / 2
"""
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        sum_nums_missing = sum(nums)
        sum_nums = n * (n+1) / 2 

        return int(sum_nums - sum_nums_missing)