"""
Brute Force O(N^2) O(1)
for every i, we need left max (0, i) and right max (i+1, n-1)
possible amount of water to be store in i would be min(leftmax, rightmax) - height[i]
accumulate this to current sum. 

if not height:
            return 0

        curr_sum = 0 

        for i in range(len(height)):
            left_max = right_max = height[i]
            # get leftmax from 0 to i 
            for l in range(i):
                left_max = max(left_max, height[l])
            # get rightmax from i+1 to len(height)-1 
            for r in range(i+1, len(height)):
                right_max = max(right_max, height[r])
            
            curr_sum += min(left_max, right_max) - height[i]
        return curr_sum

Prefix, Suffix max 
we can memoize prefix, suffix max in separate memory 
calculate pre/suf max in each i. 
"""
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left_max = [0] * n
        right_max = [0] * n

        left_max[0] = height[0]
        for i in range(1, n):
            left_max[i] = max(left_max[i - 1], height[i])
        
        right_max[n-1] = height[n-1]
        for i in range(n-2, -1, -1): 
            right_max[i] = max(right_max[i+1], height[i])
        
        result = 0
        for i in range(n):
            result += min(left_max[i], right_max[i]) - height[i]
            
        return result


            
            




        