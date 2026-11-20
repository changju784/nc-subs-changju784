"""
input: two strings s and t
output: how many string in t can be appended at the end of s to make t becomes subseq of s 
ex) coaching coding -> coachingding
cat catting -> catting 
abcde -> a 
Two pointers 
Starting two pointers from each string 
    left pointer keeps moving 
    move right pointer only when s[l] and t[r] are same 

"""
class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        i, j = 0, 0

        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                i += 1
        return len(t) - j
        