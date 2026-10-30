"""
Brute Force O(N^3) O(1)
for every substring check every substring is palindrome or not 
def longestPalindrome(self, s: str) -> str:
        def isPalindrome(l, r):
            while l < r: 
                if s[l] != s[r]: 
                    return False 
                l += 1
                r -= 1
            return True 
        max_palindrome = ""
        max_len = 0

        for i in range(len(s)):
            for j in range(i, len(s)):
                if isPalindrome(i, j):
                    if j - i + 1 > max_len:
                        max_palindrome = s[i:j+1]
                        max_len = j - i + 1
        return max_palindrome 


Two pointers 
Instead starting from both end,
expand substring from the center 
Odd/Even. 
given i, check if i-1, i+1 exists within boundary of string 
if i-1 and i+1 are same -> odd palindrome 
if i and i-1 are same or i and i+1 are same -> even palindrome 
if it's even palindrome, we should expand from both.
"""
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        resIdx, resLen = 0, 0

        for i in range(n-1, -1 ,-1):
            for j in range(i, n):
                if s[i] == s[j] and (j-i <=2 or dp[i+1][j-1] == True): 
                    dp[i][j] = True 
                    if resLen < (j - i + 1): 
                        resIdx = i 
                        resLen = j - i + 1
        
        return s[resIdx: resIdx + resLen]





        