
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curr_max = nums[0]
        curr_min = nums[0]
        result = nums[0]
        """
        [2,4,-3,5]
        cp = 8 * -3 
        cx = 8
        cn = -24
        """
        for i in range(1, len(nums)):
            new_max = max(nums[i], curr_max * nums[i], curr_min * nums[i])
            new_min = min(nums[i], curr_max * nums[i], curr_min * nums[i])
            curr_max, curr_min = new_max, new_min 
            result = max(result, curr_max)
        return result







