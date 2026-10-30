class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        Binary Search O(logN) O(1)
        1. Two segments of sorted array 
        2. Compare mid and l/r to determine minimum is located in fh or sh 
            If mid > r -> search second half -> move left to mid 
            If mid <= r -> search first half -> move right to mid 
            [3,4,5,6,1,2]
            [5,6,1,2,3,4]
        """
        l, r = 0, len(nums)-1
        while l < r: 
            mid = (l + r) // 2 
            if nums[mid] > nums[r]:
                l = mid + 1 
            else: 
                r = mid
        return nums[l]