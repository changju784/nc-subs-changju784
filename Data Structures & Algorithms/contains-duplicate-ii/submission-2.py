"""
Hashmap key- number value - index 
if not found in hashmap 
    record the hashmap[num] = i 
otherwise, 
    check if absolute index diff is <= k 
TC: O(n)
SC: O(n)
^^^ 
not working for multiple duplicates ex) [1, 0, 1, 1]
"""
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        mp = {}

        for i in range(len(nums)):
            if nums[i] in mp and i - mp[nums[i]] <= k:
                return True
            mp[nums[i]] = i

        return False
        