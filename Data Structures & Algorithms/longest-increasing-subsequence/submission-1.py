import bisect
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # This is not finding global max or min 
        # Dynamic programming 
        # From each element check what would be the LIS
        # dp = [1] * len(nums)

        # for i in range(len(nums)): 
        #     for j in range(i): 
        #         if nums[j] < nums[i]: 
        #             # update dp
        #             dp[i] = max(dp[i], dp[j]+1)
        # return max(dp)

        sub = []
        for i in range(len(nums)): 
            # if bisect idx is end of the array -> curr element is largest
            # append it 
            # otherwise, replace it with rightmost ele. 
            idx = bisect.bisect_left(sub, nums[i])
            if idx == len(sub): 
                sub.append(nums[i])
            else: 
                sub[idx] = nums[i]
        return len(sub)
            
       
                     
