"""
input: nums [1, n] with duplicates 
output: duplicate number 

Hashset O(N) O(N)
While scanning the num if num appeared in set return that number 

"""
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        hash_set = set() 
        for num in nums: 
            if num in hash_set: 
                return num 
            hash_set.add(num)
        