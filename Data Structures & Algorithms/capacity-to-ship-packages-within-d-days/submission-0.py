"""
input: int list weight, int days 
output: maximum weight to send entire weight within days constraint. 

Range of the weights 
max(weights) <= maximum weight <= sum(weights) // days

helper function to simulate 
    check if given max weight can send all weights within days 
    create a max heap of weights
        pop max heap until the sum reaches max weight 
        if reached increment day counter 
        check if day exceeded day constraints

binary search to recursively pick mid of the max weight btw its range 
    if range[mid] works, we can try smaller max weight 
        move right pointer to mid 
    else, we should try larger max weight 
        move left pointer to mid 
"""
import heapq 
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def canShipWithMax(max_weight: int):
            day, curr = 1, 0
            for w in weights: 
                if curr + w > max_weight:
                    day += 1
                    curr = w
                else: 
                    curr += w 
            return day <= days

            
        # binary search to find max weight 
        l, r = max(weights), sum(weights)
        while l < r: 
            mid = (l + r)// 2
            if canShipWithMax(mid):
                r = mid 
            else:
                l = mid + 1
        return l
            
         




        