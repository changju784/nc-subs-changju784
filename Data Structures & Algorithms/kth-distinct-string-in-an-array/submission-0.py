"""
k represent the frequency + order (index)
1. Order the arr with least frequently appeared. 
2. If there are same frequency, consider index 

What we need to store
- Frequency 
- Earliest Index
- Corresponding char 

Hashmap freq 
key - char, value - (freq, earliest index)

Iterate through hashmap 
store (freq, index) in Min heap of size of k 

"""
from collections import defaultdict
class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        hash_map = defaultdict(int)
        for c in arr: 
            hash_map[c] += 1
        
        for c in arr: 
            if hash_map[c] == 1: 
                # decrement k 
                k -= 1
                if k == 0: 
                    return c     
        return ''