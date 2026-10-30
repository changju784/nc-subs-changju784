"""
Key Points 
1. letters in t could be duplicate and each should be covered in s 
2. cannot guarantee with indices, earliest or latest does not matter to get shortest substring. 
    - hashmap to store frequency
Sliding window using two pointers 
record minimum window size or the substring so far once current window fulfills the conditions 

Sliding window 
iterating through list 
record frequecy table, current frequency, and minimum length as well as starting and endpoint. 
first moving right and if found in freq table,
only increment curr_freq when corresponding freq in table is positive. 
!! if freq positive -> window not fulfilled, if freq negative -> we have already fulfilled and have surplus. 
once fulfilled, move right (shrink) the window 

"""
from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return "" 
        # get frequency table 
        freq = defaultdict(int)
        for c in t: 
            freq[c] += 1
        
        # sliding window 
        minimum_length = float('inf')
        curr_freq, l, res = 0, 0, (0, 0)

        for r, c in enumerate(s):
            # when r found in table
            if c in freq: 
                if freq[c] > 0:
                    curr_freq += 1 
                freq[c] -= 1
                # move l
                while curr_freq == len(t): 
                    if curr_freq == len(t): # fulfilled condition
                        if (r-l+1) < minimum_length:
                            minimum_length = r-l+1
                            res = (l, r)

                    if s[l] in freq: 
                        freq[s[l]] += 1
                        if freq[s[l]] > 0: 
                            curr_freq -= 1
                    l += 1

        if minimum_length == float('inf'):
            return ""
        return s[res[0]: res[1]+1]

            
        