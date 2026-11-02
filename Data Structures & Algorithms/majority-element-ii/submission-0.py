"""
hashmap key-num val-freq
"""
from collections import defaultdict 
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        hash_map = defaultdict(int)
        for num in nums: 
            hash_map[num] += 1
        
        result = []
        for k, v in hash_map.items(): 
            if v > (len(nums)/3): 
                result.append(k)
        return result

        