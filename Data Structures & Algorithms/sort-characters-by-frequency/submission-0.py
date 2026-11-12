"""
Iterate through s and build freq table 


"""
from collections import defaultdict
class Solution:
    def frequencySort(self, s: str) -> str:
        freq = defaultdict(int)
        for c in s: 
            freq[c] += 1
        sorted_freq = sorted([(v, k) for k, v in freq.items()], reverse=True)
        result = "" 
        for f, v in sorted_freq: 
            result += v * f 

        return result

        