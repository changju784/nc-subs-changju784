class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # pass prefix products 
        # pass suffix products 

        # [1, 2, 4, 6]
        # p = [1, 1, 2, 8]
        # s = [48, 24, 6, 1]

        prefix_prods = [1] * len(nums)
        suffix_prods = [1] * len(nums)
        prefix_prod = 1
        suffix_prod = 1

        for i in range(1, len(nums)): 
            prefix_prod *= nums[i-1]
            prefix_prods[i] = prefix_prod
        
        for i in range(len(nums)-2, -1, -1):
            suffix_prod *= nums[i+1]
            suffix_prods[i] = suffix_prod

        return [p * s for p, s in zip(prefix_prods, suffix_prods)]
