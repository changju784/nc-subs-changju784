"""
Permutation cab -> abc, same freq, diff order 
input: 2 strings 
output: boolean if s2 contains permutation of s1 

abc lecabee
      ^ ^
frequency only matters 

Brute Force 
Build frequency table 
    1. hashmap key - char, val - freq {a:1, b:1, c:1}
    2. Or 26 count array abc = [1,1,1,0,0 ...]
Generate all substrings from s2 
    Check if that count/hashmap matches with s1 

N, M = len(s1), len(s2)
Time complexity: O(N + M^2)
SC: O(N)

Sliding window -> TC: O(N + M) 
After building map from s1 
Window of size S1 
Right pointer keep adding to map counter up 
Left pointer count down 
Once they are matching with the map from s1, permutation found
"""
class Solution:

    def checkInclusion(self, s1: str, s2: str) -> bool:
        # if s1 is bigger, no permutation 
        if len(s1) > len(s2): 
            return False 

        # build freq table from s1
        freq_s1 = [0] * 26 
        for c1 in s1: 
            freq_s1[ord(c1) - ord('a')] += 1
        
        # sliding window size of s1 
        l = 0
        freq_s2 = [0] * 26 
        for r in range(len(s2)):
            # if current freq window is same as s1, perm found 
            if freq_s2 == freq_s1: 
                return True 
            # count up from right pointer 
            freq_s2[ord(s2[r]) - ord('a')] += 1

            # count down from left pointer 
            if r >= len(s1): 
                freq_s2[ord(s2[l]) - ord('a')] -= 1
                l += 1
        # after iteration when freq not found, return False 
        return freq_s2 == freq_s1

            

        


