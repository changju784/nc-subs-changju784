class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        1. Two segments of sorted array 
        2. compare l, r with mid 
            if mid >= r -> second half if mid < r -> first half 
        
        1. Find two segments of sorted array 
        2. Find target form according segment 
        Binary Search O(logn) O(1)

        [6, 1, 2, 3, 4, 5] target = 2
        nums = [3,4,5,6,1,2], target = 1
                ^   ^     ^ 
        """
        l, r = 0, len(nums)-1 
        while  l <= r: 
            mid = (l + r)//2 
            if nums[mid] == target:
                return mid 

            if nums[l] <= nums[mid]: # fh sorted
                if nums[l] <= target < nums[mid]: # target located in fh
                    r = mid - 1
                else: 
                    l = mid + 1
            else: 
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else: 
                    r = mid - 1

        return -1
