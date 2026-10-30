"""
input: nums [1, n] with duplicates 
output: duplicate number 

Hashset O(N) O(N)
While scanning the num if num appeared in set return that number 

Negative marking 
since each number [1, n] can represent the index, we can mark negative to that index.
while scan the number 
    if the number is negative, return abs(num) + 1
mark the number as negative. 
"""
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for num in nums: 
            idx = abs(num) - 1
            if nums[idx] < 0: 
                return idx + 1
            nums[idx] *= -1
        