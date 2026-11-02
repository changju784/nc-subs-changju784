"""
Sorting + Two Pointers O(nlogn) O(1)
sort the people by ascending order 
left and right pointers -> 
    get remaining weight after having right person 
    increment boat counter and decrement r 
    if l <= remaining increment l 
"""
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort() 
        l, r = 0, len(people)-1 
        boat = 0 

        while l <= r:
            remaining = limit - people[r]
            r -= 1
            if l <= r and people[l] <= remaining: 
                l += 1
            boat += 1
        return boat
