"""
Sort + Two Pointers O(N^2) O(N)
First sort the list 
Iterate through the list 
    For each number we set left pointer right after i and right pointer till the end 
    if current sum (num + nums[l] + nums[r]) > target -> move right pointer 
    otherwise move left pointer 
"""
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() 
        result = []

        for i, num in enumerate(nums):
            if num > 0:
                break  
            if i > 0 and num == nums[i-1]:
                continue

            l, r = i + 1, len(nums)-1 
            while l < r:
                curr_sum = num + nums[l] + nums[r]
                if  curr_sum > 0: # sum is too much, reduce by moving r 
                    r -= 1
                elif curr_sum < 0: # sum is too low, increase by moving l 
                    l += 1
                else: 
                    # append, move both pointer, move left until no dup
                    result.append([num, nums[l], nums[r]])
                    l += 1 
                    r -= 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
        return result

