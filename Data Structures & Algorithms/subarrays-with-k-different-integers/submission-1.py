"""
input: integer list nums and integer k 
output: find number of subarrays whose element is k unique numbers. 

Brute Force O(N^2) O(N)
For each element try generating all subarrays 
    while generating subarrays, 
        check how many distinct numbers being used 
        if it's exactly k numbers, append to the result 

Sliding window 
right pointer approaches end 
    add right pointer num[r] to set
    if len(set) exceeded k 
    while len(set) > k: 
        remove leftpointer element from the set 
        move left pointer to right 
    if len(set) == k: 
        increment subarray count
"""
class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:

        def atMostK(k):
            count = defaultdict(int)
            res = l = 0

            for r in range(len(nums)):
                count[nums[r]] += 1
                if count[nums[r]] == 1:
                    k -= 1

                while k < 0:
                    count[nums[l]] -= 1
                    if count[nums[l]] == 0:
                        k += 1
                    l += 1

                res += (r - l + 1)

            return res

        return atMostK(k) - atMostK(k - 1)



        