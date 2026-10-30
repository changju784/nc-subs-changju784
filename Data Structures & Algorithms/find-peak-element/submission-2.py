"""
input - integer array (could be neg) outerbounds are all neg inf 
output - any index where peak exists. 

def peak -> if nums[i-1] < nums[i] < nums[i+1]

[1,2,3,1]
   ^
Brute Force O(N) O(1)
Scan the array 
    find the downhill -> if i+1 is smaller than i -> i is a peak 

[1, 2, 0, 3, 1]
    L
    M 
    R

Binary Search 
1. see if m is a peak -> need to compare m-1 and m+1 -> if m-1 < m & m+1 < m
2. if m is not a peak -> if m-1 > m || m+1 > m

while l <= r: 
    mid = (l + r) // 2
    # see if m is a peak 
    if m > 0 and m < len(nums) and m > m-1 and m > m+1 return m 
    else: 
        if m > 0 and m-1 > m -> peak in fh -> move right pointer to mid -1 
        else m < len(nums) and m+1 > m -> peak in sh -> move left pointer to mid +1

"""
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        while l <= r: 
            m = (l + r) // 2
            # peak is in fh, move right pointer to mid
            if m > 0 and nums[m] < nums[m-1]: 
                r = m - 1
            # peak is in sh, move left pointer to mid
            elif m < len(nums)-1 and nums[m] < nums[m+1]:
                l = m + 1
            else: 
                return m

            