# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

"""
Binary Search 
range - 1 to n 
keep getting mid number 
if guess mid number == 0 return that 
if guess mid number == -1  -> search first half -> move r to mid 
if guess mid number == 1 -> search second half -> move l to mid + 1

"""

class Solution:
    def guessNumber(self, n: int) -> int:
        l, r = 1, n 
        while l <= r: 
            mid = (l + r) // 2
            if guess(mid) == 0:
                return mid 
            elif guess(mid) == -1: 
                r = mid 
            else: 
                l = mid + 1
            
        