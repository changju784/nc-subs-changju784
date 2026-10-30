"""
Brute Force O(N^3) O(1)
Try all the substrings and see if they are palindromes.
Iterate through each char, 
    iterate through other pair, i+1 to end 
    check if that two pointers l, r gives palindrome. 

def countSubstrings(self, s: str) -> int:
        def isPalindrome(l, r):
            while l < r: 
                if s[l] != s[r]:
                    return False 
                l += 1 
                r -= 1
            return True 

        answer = 0
        for l in range(len(s)): 
            for r in range(l, len(s)):
                if isPalindrome(l, r): 
                    answer += 1
        return answer

DP bottom-up 
we can have 2d dp represents l and r
if we want to know if s[l:r] is palindrome, we can check s[l+1][r-1]. 
iterating l from n-1 to 0 
    iterating r from i to n-1 
        if substring -> s[l] == s[r] and (l-r+1 <= 2 or s[l+1][r-1] == True)
            mark dp[l][r] = true 
            count up palindrome substring 
        


"""
class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        palindrome_substrings = 0

        for l in range(n-1, -1, -1): 
            for r in range(l, n):
                # if start of the palindrome -> "aba"
                # or previous l+1 r-1 was palindrome
                if s[l] == s[r] and (r-l+1 <= 2 or dp[l+1][r-1] == True):
                    dp[l][r] = True 
                    palindrome_substrings += 1
        return palindrome_substrings 




        