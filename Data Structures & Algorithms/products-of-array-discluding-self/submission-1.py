class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # pass prefix products 
        # pass suffix products 

        # [1, 2, 4, 6]
        # p = [1, 1, 2, 8]
        # s = [48, 24, 6, 1]

        result = [1] * len(nums)
        suffix_prod = 1

        for i in range(1, len(nums)): 
            result[i] = result[i-1] * nums[i-1]
        
        for i in range(len(nums)-2, -1, -1):
            suffix_prod *= nums[i+1]
            result[i] *= suffix_prod

        return result
