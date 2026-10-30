class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        """
        kuberenetes - k8s
        Key points 
        1. Leading zero is invalid 
        2. Entire substring could be number 
        3. Entire substring may not contain any number 

        "apple" "5"
             l       r    
        skip_num = 11
        Two Pointers
        Set two pointers for word and abbr 
        while both pointers towards the end 
            when they are same: move both pointers
            when they are different 
                while r faces with num accumulate skipnum 
                if skipnum is 0 or l+skip_num > len(word) -> return false 
                move left pointer to amount of skipnum 
                resset skip_num to 0
        return true 

        Time Complexity: O(max(n, m)) 
        Space Complexity: O(1)
        """
        l, r = 0, 0
        skip_num = 0

        while l < len(word) and r < len(abbr): 
            if word[l] == abbr[r]:
                l += 1
                r += 1
            else: 
                if abbr[r] == '0':
                    return False 
                while r < len(abbr) and abbr[r].isnumeric(): 
                    skip_num *= 10
                    skip_num += int(abbr[r])
                    r += 1
                if skip_num == 0 or l + skip_num > len(word):
                    return False 
                l += skip_num
                skip_num = 0 
        return l == len(word) and r == len(abbr) 

                

            
