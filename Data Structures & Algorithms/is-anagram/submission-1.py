class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        1. sorting 
        if len(s) != len(t): 
            return False 

        s = sorted(s)
        t = sorted(t)
        return s == t

        2. hash - three passes
        using ascii count array

        """
        if len(s) != len(t): 
            return False 
        
        counts = [0] * 26

        for i in range(len(s)):
            char_s = s[i]
            char_t = t[i] 
            counts[ord(char_s) - ord('a')] += 1 
            counts[ord(char_t) - ord('a')] -= 1 
        
        for c in counts: 
            if c != 0: 
                return False         
        return True

        
        