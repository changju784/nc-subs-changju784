class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Brute Force
        # for i in range(len(nums)): 
        #     for j in range(i+1, len(nums)): 
        #         if nums[i] + nums[j] == target: 
        #             return [i, j]

        # Hashmap 
        # store key = target - num val as index 
        hash_map = {} 
        for i in range(len(nums)): 
            if nums[i] not in hash_map: 
                hash_map[target - nums[i]] = i 
            else: 
                return [hash_map[nums[i]], i]

        

