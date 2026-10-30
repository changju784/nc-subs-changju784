class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        sliding window 
        lookup table to record latest index char appeared 
        right pointer keep iterating through the string 
        once we have found the existing char, move left pointer to right after latest
        index.
        keep update max_len every iteration 
        keep record latest index of char found 

        "zxyzxyz"
           l
             r
        hash_map = {z: 3, x: 4, y: 5} 
        max_len = 3
        """
        if len(s) == 0: 
            return 0 
        hash_map = {} # key - char val - lastest idx char found 
        max_len = 0 
        l = 0 

        for r, c in enumerate(s): 
            if c in hash_map and hash_map[c] >= l: 
                l = hash_map[c] + 1
            hash_map[c] = r 
            max_len = max(max_len, r - l + 1)
        return max_len 

        

