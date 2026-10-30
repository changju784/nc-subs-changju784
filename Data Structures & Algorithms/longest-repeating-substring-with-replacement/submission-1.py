from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        Key Points 
        1. 0 <= k < len(s)
        2. s consist of only UPPER alphabets 
        3. substring contiguous same chars 
        4. return longest substring with same chars after replacement
        5. Most frequent -> best candidate 
        6. Sliding window -> dynamic window size: # most frequent chars + k (non-mfc)
        7. we need to memoize how many mfc contains in current window 
        
        s = "BBAAABABB", k = 1
                  l
                  r
        mfc_count = 3
        window_size(r-l+1) = 5
        max_length = 4

        Whenever r faces with mfc: 
            mfc += 1
            Update max_length 
        Whenever r faces with non-mfc:
            If mfc_count is less than window_size - k:
                Move left pointer -> r
                reset mfc_count 
            else:
                Update max_length
        """
        # Slicing window 
        freq = [0] * 26
        max_length = 0 
        l = 0 
        for r, c in enumerate(s): 
            freq[ord(c)-ord('A')] += 1
            mfc_count = max(freq)
            while (r-l+1) - mfc_count > k: 
                freq[ord(s[l])-ord('A')] -= 1
                l += 1 
            max_length = max(max_length, r-l+1) 
        return max_length


        