"""
Key points 
1. only applies strictly for substring and order matters 
2. can reuse

"hellow" ["ello", "hw"]
Brute Force 
iterate through string and we accumulate the substring,
whenever substring found in word dict (set)
after iteration check the length of set if it's not empty return False 
"neetcode", wordDict = ["neet","code"] -> {'code'}
        ^
curr_string = "c"

dfs
Try every word in dict 
if a word matches the string at i, recursively check remaining substring can also be broken
basecase - when reaches the end of string len(s) return True 
params - i 
def dfs(i):
    if i == len(s):
        return True 
    
    for word in wordDict: 
        if i + len(word) <= len(s) and s[i: i+len(word)] == word:
            if dfs(i + len(word)):
                return True 
    return False 
return dfs(0)

DP top-down memoization 
From recurison, we noticed i (where suffix s[i:] be segmented) reaching many times 
result of dfs(i) never changes, so we can memoize. 
from hashmap dp[i] represent if i can be segmented. 


"""
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = {len(s): True }
        def dfs(i):
            if i in dp:
                return dp[i]
            
            for word in wordDict: 
                if i + len(word) <= len(s) and s[i: i+len(word)] == word:
                    if dfs(i + len(word)):
                        dp[i] = True 
                        return True 
            dp[i] = False 
            return False 
        return dfs(0)
