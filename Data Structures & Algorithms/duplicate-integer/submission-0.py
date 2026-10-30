class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # extra space hash set 
        return len(nums) != len(set(nums))