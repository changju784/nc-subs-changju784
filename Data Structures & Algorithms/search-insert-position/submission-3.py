"""
input: a sorted integer array, integer target 
output: index where target located in the array 

[-1, 0, 2, 4, 6] target = 3 -> 2
           
Linear scan O(N) O(1)
While scanning the int array 
    Check if current value is smaller or larger 
    Find the num where value gets greater or equal than target

Binary Search O(logN) O(1)
Given two pointers starting from both end, 
    Keep compute the mid pointer 
    Compare the mid pointer with target 
    If the value of mid pointer > target 
        search first half by moving right p to mid 
    If the value of mid p < target 
        search second half by moving left p to mid 
"""
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)
        while l < r: 
            mid = (l + r) // 2
            if nums[mid] >= target: 
                r = mid
            elif nums[mid] < target: # search sh 
                l = mid + 1
            
        return l
            

        