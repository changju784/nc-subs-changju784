class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        1. sorting 
        if len(s) != len(t): 
            return False 

        s = sorted(s)
        t = sorted(t)
        return s == t

        2. ascii count array 
        iterate through two strings using index. 
        one count up ascii index, other count down. 
        check if count array contains 1s. 

        """
        if len(s) != len(t): 
            return False 
        
        counts = [0] * 26

        for char_s, char_t in zip(s, t): 
            counts[ord(char_s) - ord('a')] += 1 
            counts[ord(char_t) - ord('a')] -= 1 
        
        for c in counts: 
            if c != 0: 
                return False 
        return True 


        
        