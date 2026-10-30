class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * (n * 2)
        for i in range(len(nums)):
            result[i] = nums[i]
            result[i+n] = nums[i]
        return result
