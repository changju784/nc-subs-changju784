"""
input - binary array 
output - max length of consecutive 1s. 
Key points 
1. contiguous 
2. order (index) matters 

constraints: 
1 <= length of nums < 10**5
nums[i] = only 1 or 0 
[1,1,0,1,0,1,1,1]  
               ^

[1] [0] [11] [00]
              ^
current_sum = 0
max_sum = 0

Brute Force O(N) O(1)
while iterating through the binary list:
    whenever we face with 1: 
        add this to current sum 
    whenever we face with 0: 
        update the global maximum compare it with current sum 
        reset the current sum to 0
return max(max_sum, curr_sum)


"""
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        curr_sum = 0 
        max_sum = 0 
        for num in nums: 
            if num == 1: 
                curr_sum += 1
            else: 
                max_sum = max(max_sum, curr_sum)
                curr_sum = 0 
        return max(max_sum, curr_sum)