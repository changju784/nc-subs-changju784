"""
1. list slicing O(n) O(n)
return nums[len(nums) - k:] + nums[0:len(nums) - k]
2. pop and append k amount. O(n*k) O(1)
3. reverse the list. O(n) O(1)
we need to re-reverse two separate array 
from 0:k and k:
helper function two pointers 
[1,2,3,4,5,6,7] k = 2
[7,6,5,4,3,2,1] [7,6] [5,4,3,2,1] 
[6,7,1,2,3,4,5]

[1,2,3,4,5] 
   l
       r

"""

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverse(l, r):
            while l < r: 
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
             
        if k > len(nums): 
            k %= len(nums)
        
        # 1. reverse entire array
        nums.reverse()
        # 2. re-reverse two segments using two pointers 
        reverse(0, k-1)
        reverse(k, len(nums)-1)
        
    
        